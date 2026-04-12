import pytest
from django.urls import reverse
from parameterized import parameterized

from auth.models import User
from common.tests.fixtures import user  # noqa: F401, F811
from company.tests.factories import CompanyFactory

from ..models import Agency
from .factories import AgencyFactory


@pytest.mark.django_db
class TestAgency:
    @pytest.fixture(autouse=True)
    def setup(self, client, user):
        self.company = CompanyFactory()
        user.company = self.company
        user.save()
        client.force_login(user)
        self.client = client
        self.agency = AgencyFactory(company=self.company)
        self.create_url = reverse("agency:agency_create")
        self.update_url = reverse(
            "agency:agency_update",
            kwargs={"pk": self.agency.pk},
        )
        self.delete_url = reverse(
            "agency:agency_delete",
            kwargs={"pk": self.agency.pk},
        )

    def test_return_list_ok(self, client):
        response = client.get(reverse("agency:agency_list"))
        assert str(self.agency.name) in response.text
        assert response.status_code == 200

    def test_not_return_other_user_company_agency(self, client):
        new_user = User.objects.create_user(
            username="newuser",
            password="strongpassword",
        )
        new_user.refresh_from_db()
        client.force_login(new_user)
        response = client.get(reverse("agency:agency_list"))
        assert str(self.agency.name) not in response.text

    def test_create_agency_ok(self, client):
        response = client.post(
            self.create_url,
            {"name": "Galileo", "ceo": "Joh Doe"},
        )
        assert response.status_code == 302
        assert Agency.objects.filter(name="Galileo", company=self.company).exists()

    def test_create_agency_missing_name(self, client):
        response = client.post(
            self.create_url,
            {"name": "", "ceo": "Joh Doe"},
        )
        assert response.status_code == 302
        assert not Agency.objects.filter(ceo="Joh Doe", company=self.company).exists()

    def test_update_agency_ok(self, client):
        assert not self.agency.name == "Galileo"

        client.post(self.update_url, {"name": "Galileo"})

        self.agency.refresh_from_db()
        assert self.agency.name == "Galileo"

    def test_update_agency_not_ok(self, client):
        response = client.post(self.update_url, {})
        assert response.status_code == 302

    def test_delete_agency_ok(self, client) -> None:
        client.post(self.delete_url)
        assert self.company.agencies.count() == 0

    def test_cant_delete_other_company_agency(self, client) -> None:
        assert self.company.agencies.count() == 1

        other_company = CompanyFactory()
        other_agency = AgencyFactory(company=other_company)
        client.post(
            reverse(
                "agency:agency_delete",
                kwargs={"pk": other_agency.pk},
            ),
        )

        assert self.company.agencies.count() == 1

    @parameterized.expand(
        (
            ["agency:agency_list", None],
            ["agency:agency_create", None],
            ["agency:agency_delete", {"pk": 1}],
            ["agency:agency_update", {"pk": 1}],
        )
    )
    def test_user_must_be_authenticated(self, url, kwargs) -> None:
        self.client.logout()
        response = self.client.get(reverse(url, kwargs=kwargs))
        assert response.status_code == 302
