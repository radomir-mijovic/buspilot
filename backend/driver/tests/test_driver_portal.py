import pytest
from django.urls import reverse
from parameterized import parameterized

from auth.models import UserTypeChoices
from common.tests.fixtures import user  # noqa: F401, F811
from company.tests.factories import CompanyFactory
from vehicle.tests.factories import VehicleFactory

from .factories import DriverFactory


@pytest.mark.django_db
class TestDrivers:
    @pytest.fixture(autouse=True)
    def setup(self, client, user):  # noqa: F401, F811
        self.user = user
        self.user.user_type = UserTypeChoices.DRIVER
        self.user.save()
        client.force_login(self.user)
        self.client = client
        self.company = CompanyFactory()
        user.company = self.company
        self.vehicle = VehicleFactory(company=self.company)
        user.save()

        self.report_defect_url = reverse("driver_api:driver_portal-report-defects")

    def test_driver_report_defect_successfully(self):
        response = self.client.post(
            self.report_defect_url,
            {
                "description": "Defect description",
                "vehicle": self.vehicle.pk,
            },
        )
        assert response.status_code == 201
        assert response.data.get("details") == "Report successully reported."

    def test_field_vehicle_is_required(self):
        response = self.client.post(
            self.report_defect_url,
            {
                "description": "Defect description",
            },
        )
        assert response.status_code == 400
        assert response.data.get("vehicle")[0] == "This field is required."

    def test_field_vehicle_may_not_be_null(self):
        response = self.client.post(
            self.report_defect_url,
            {"description": "Defect description", "vehicle": ""},
        )
        assert response.status_code == 400
        assert response.data.get("vehicle")[0] == "This field may not be null."

    def test_field_description_may_not_be_blank(self):
        response = self.client.post(
            self.report_defect_url,
            {"description": "", "vehicle": self.vehicle.pk},
        )
        assert response.status_code == 400
        assert response.data.get("description")[0] == "This field may not be blank."

    def test_field_description_is_required(self):
        response = self.client.post(
            self.report_defect_url,
            {
                "vehicle": self.vehicle.pk,
            },
        )
        assert response.status_code == 400
        assert response.data.get("description")[0] == "This field is required."

    def test_cant_report_other_vehicle_defect(self):
        vehicle = VehicleFactory()
        response = self.client.post(
            self.report_defect_url,
            {
                "vehicle": vehicle.pk,
            },
        )
        assert response.status_code == 400
        assert (
            response.data.get("vehicle")[0]
            == f"Object with id={vehicle.id} does not exist."
        )
