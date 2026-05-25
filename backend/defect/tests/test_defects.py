import pytest
from django.urls import reverse

from auth.tests.factories import UserFactory
from common.tests.fixtures import user
from company.tests.factories import CompanyFactory
from defect.models import Defect
from driver.tests.factories import DriverFactory  # noqa: F401, F811
from vehicle.tests.factories import VehicleFactory

from .factories import DefectFactory


@pytest.mark.django_db
class TestDefect:
    @pytest.fixture(autouse=True)
    def setup(self, client, user):
        client.force_login(user)
        self.client = client
        self.company = CompanyFactory()

        self.user = user
        self.user.company = self.company
        self.user.save()

        self.driver = DriverFactory()
        self.driver.company = self.company
        self.company.save()

        self.vehicle = VehicleFactory(company=self.company)

        self.defect = DefectFactory(company=self.company)
        self.list_url = reverse("defect:defects")
        self.create_url = reverse("defect:defect_create")

    def test_return_list_ok(self):
        response = self.client.get(self.list_url)
        assert self.defect.description in response.text

    def test_list_filter_ok(self):
        other_company = CompanyFactory()
        other_defect = DefectFactory(company=other_company)
        response = self.client.get(self.list_url)
        assert other_defect.description not in response.text

    def test_driver_create_defect_ok(self):
        assert Defect.objects.count() == 1
        self.client.post(
            self.create_url,
            {
                "description": "Defect description",
                "vehicle": self.vehicle.pk,
            },
        )
        assert Defect.objects.count() == 2

    def test_mark_defect_as_resolved_ok(self):
        self.defect.is_fixed = False
        self.defect.save()

        assert not self.defect.is_fixed
        self.client.post(
            reverse(
                "defect:mark_as_resolved",
                kwargs={"pk": self.defect.pk},
            ),
            {"is_fixed": True},
        )
        self.defect.refresh_from_db()
        assert self.defect.is_fixed

    def test_mark_defect_as_not_resolved(self):
        self.defect.is_fixed = True
        self.defect.save()

        assert self.defect.is_fixed
        self.client.post(
            reverse(
                "defect:mark_as_resolved",
                kwargs={"pk": self.defect.pk},
            ),
            {"is_fixed": False},
        )
        self.defect.refresh_from_db()
        assert not self.defect.is_fixed

    def test_delete_defect_ok(self):
        assert Defect.objects.count() == 1
        self.client.post(
            reverse(
                "defect:defect_delete",
                kwargs={"pk": self.defect.pk},
            )
        )
        assert Defect.objects.count() == 0

    def test_cant_delete_other_company_defect(self):
        other_user = UserFactory()
        other_user.company = CompanyFactory()
        other_user.save()

        self.client.force_login(other_user)

        assert Defect.objects.count() == 1
        self.client.delete(
            reverse("defect:defect_delete", kwargs={"pk": self.defect.pk})
        )
        assert Defect.objects.count() == 1
