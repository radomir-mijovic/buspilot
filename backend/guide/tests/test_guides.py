import pytest
from django.urls import reverse
from parameterized import parameterized

from common.tests.fixtures import user  # noqa: F401, F811
from company.tests.factories import CompanyFactory

from .factories import GuideFactory


@pytest.mark.django_db
class TestGuides:
    @pytest.fixture(autouse=True)
    def setup(self, client, user):  # noqa: F401, F811
        client.force_login(user)
        self.client = client
        self.company = CompanyFactory()
        user.company = self.company
        user.save()
        self.guide = GuideFactory(company=self.company)
        self.list_url = reverse("guide:guides")
        self.create_url = reverse("guide:guides_create")
        self.update_url = reverse(
            "guide:guide_update",
            kwargs={"pk": self.guide.pk},
        )
        self.delete_url = reverse(
            "guide:guide_delete",
            kwargs={"pk": self.guide.pk},
        )

    def test_return_list_ok(self, client):
        response = client.get(self.list_url)
        assert self.guide.first_name in response.text

    def test_list_filter_ok(self, client):
        other_company = CompanyFactory()
        other_guide = GuideFactory(company=other_company)
        response = client.get(self.list_url)
        assert other_guide.first_name not in response.text

    def test_create_guide_ok(self, client):
        assert self.company.guide_items.count() == 1
        client.post(
            self.create_url,
            {
                "first_name": "John",
                "last_name": "Doe",
            },
        )
        assert self.company.guide_items.count() == 2

    def test_create_guide_not_ok(self, client):
        assert self.company.guide_items.count() == 1
        respone = client.post(self.create_url, {})
        assert self.company.guide_items.count() == 1
        assert respone.status_code == 302

    def test_update_guide_ok(self, client):
        assert not self.guide.first_name == "Mike"
        assert not self.guide.last_name == "Tyson"

        client.post(
            self.update_url,
            {"first_name": "Mike", "last_name": "Tyson"},
        )

        self.guide.refresh_from_db()
        assert self.guide.first_name == "Mike"
        assert self.guide.last_name == "Tyson"

    def test_update_guide_not_ok(self, client):
        response = client.post(self.update_url, {})
        assert response.status_code == 302

    def test_delete_guide_ok(self, client) -> None:
        client.post(self.delete_url)
        assert self.company.guide_items.count() == 0

    def test_cant_delete_other_company_guide(self, client) -> None:
        assert self.company.guide_items.count() == 1

        other_company = CompanyFactory()
        other_guide = GuideFactory(company=other_company)
        client.post(
            reverse(
                "guide:guide_delete",
                kwargs={"pk": other_guide.pk},
            ),
        )

        assert self.company.guide_items.count() == 1

    @parameterized.expand(
        (
            ["guide:guides", None],
            ["guide:guides_create", None],
            ["guide:guide_delete", {"pk": 1}],
            ["guide:guide_update", {"pk": 1}],
        )
    )
    def test_user_must_be_authenticated(self, url, kwargs) -> None:
        self.client.logout()
        response = self.client.get(reverse(url, kwargs=kwargs))
        assert response.status_code == 302
