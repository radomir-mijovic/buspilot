import pytest
from django.urls import reverse

from common.tests.fixtures import user  # noqa: F401, F811
from company.tests.factories import CompanyFactory

from .factories import DriverFactory


@pytest.mark.django_db
class TestDrivers:
    @pytest.fixture(autouse=True)
    def setup(self, client, user):  # noqa: F401, F811
        client.force_login(user)
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

    def test_return_list_ok(self, client):
        response = client.get(self.list_url)
        assert self.driver.first_name in response.text

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
        response = client.post(
            self.update_url, {}
        )
        assert response.status_code == 302
