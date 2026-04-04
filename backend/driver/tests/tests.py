import pytest
from django.urls import reverse
from parameterized import parameterized

from common.tests.fixtures import user  # noqa: F401, F811
from company.tests.factories import CompanyFactory

from .factories import DriverFactory


@pytest.mark.django_db
class TestDrivers:
    @pytest.fixture(autouse=True)
    def setup(self, client, user):  # noqa: F401, F811
        client.force_login(user)
        self.client = client
        self.company = CompanyFactory()
        user.company = self.company
        user.save()
        self.driver = DriverFactory(company=self.company)
        self.list_url = reverse("driver:drivers")
        self.create_url = reverse("driver:drivers_create")
        self.update_url = reverse(
            "driver:driver_update",
            kwargs={"pk": self.driver.pk},
        )
        self.delete_url = reverse(
            "driver:driver_delete",
            kwargs={"pk": self.driver.pk},
        )

    def test_return_list_ok(self, client):
        response = client.get(self.list_url)
        assert self.driver.first_name in response.text

    def test_list_filter_ok(self, client):
        other_company = CompanyFactory()
        other_driver = DriverFactory(company=other_company)
        response = client.get(self.list_url)
        assert other_driver.first_name not in response.text

    def test_create_driver_ok(self, client):
        assert self.company.drivers.count() == 1
        client.post(
            self.create_url,
            {
                "first_name": "John",
                "last_name": "Doe",
            },
        )
        assert self.company.drivers.count() == 2

    def test_create_driver_not_ok(self, client):
        assert self.company.drivers.count() == 1
        respone = client.post(self.create_url, {})
        assert self.company.drivers.count() == 1
        assert respone.status_code == 302

    def test_update_driver_ok(self, client):
        assert not self.driver.first_name == "Mike"
        assert not self.driver.last_name == "Tyson"

        client.post(
            self.update_url,
            {"first_name": "Mike", "last_name": "Tyson"},
        )

        self.driver.refresh_from_db()
        assert self.driver.first_name == "Mike"
        assert self.driver.last_name == "Tyson"

    def test_update_driver_not_ok(self, client):
        response = client.post(self.update_url, {})
        assert response.status_code == 302

    def test_delete_driver_ok(self, client) -> None:
        client.post(self.delete_url)
        assert self.company.drivers.count() == 0

    def test_cant_delete_other_company_driver(self, client) -> None:
        assert self.company.drivers.count() == 1

        other_company = CompanyFactory()
        other_driver = DriverFactory(company=other_company)
        client.post(
            reverse(
                "driver:driver_delete",
                kwargs={"pk": other_driver.pk},
            ),
        )

        assert self.company.drivers.count() == 1

    @parameterized.expand(
        (
            ["driver:drivers", None],
            ["driver:drivers_create", None],
            ["driver:driver_delete", {"pk": 1}],
            ["driver:driver_update", {"pk": 1}],
        )
    )
    def test_user_must_be_authenticated(self, url, kwargs) -> None:
        self.client.logout()
        response = self.client.get(reverse(url, kwargs=kwargs))
        assert response.status_code == 302
