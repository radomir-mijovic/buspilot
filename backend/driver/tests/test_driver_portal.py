from datetime import timedelta

import pytest
from django.urls import reverse
from django.utils import timezone

from auth.models import UserTypeChoices
from common.tests.fixtures import user  # noqa: F401, F811
from company.tests.factories import CompanyFactory
from driver.tests.factories import DriverFactory
from ride.tests.factories import RideFactory
from vehicle.tests.factories import VehicleFactory


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

        self.ride = RideFactory(company=self.company)
        self.ride.drivers.add(self.user.id)

        self.driver_details_url = reverse("driver_api:driver_detail-list")
        self.driver_rides_count_url = reverse("driver_api:driver_portal-rides-count")
        self.driver_url = reverse("driver_api:driver_portal-driver-details")
        self.defect_vehicles_url = reverse("driver_api:driver_portal-defect-vehicles")
        self.report_defect_url = reverse("driver_api:driver_portal-report-defects")
        self.confirm_ride_url = reverse("driver_api:driver_portal-confirm-ride")
        self.cancel_ride_url = reverse("driver_api:driver_portal-cancel-ride")
        self.pass_rides_url = reverse("driver_api:driver_portal-pass-rides")

    def test_return_driver_details_ok(self):
        driver = DriverFactory()
        self.user.user_type = UserTypeChoices.ADMIN
        self.user.save()
        response = self.client.get(self.driver_details_url)

        assert response.status_code == 200
        assert driver.id in response.data[0].values()

    def test_return_driver_portal_ok(self):
        response = self.client.get(self.driver_url)

        assert response.status_code == 200
        assert self.user.id == response.data.get("id")

    def test_return_defect_vehicles_ok(self):
        response = self.client.get(self.defect_vehicles_url)

        assert response.status_code == 200
        assert self.vehicle.id == response.data[0].get("id")

    def test_return_pass_rides_ok(self):
        pass_date = timezone.now() - timedelta(days=7)
        pass_ride = RideFactory(
            company=self.company, start_date=pass_date, end_date=pass_date
        )
        pass_ride.drivers.add(self.user.id)

        response = self.client.get(self.pass_rides_url)

        assert response.status_code == 200
        assert pass_ride.id in response.data[0].values()

    def test_future_rides_not_in_response(self):
        """The future (one is created in setUp)
        rides should not be in pass ride response"""
        response = self.client.get(self.pass_rides_url)

        assert response.status_code == 200
        assert len(response.data) == 0

    def test_return_rides_ok(self):
        response = self.client.get(self.driver_rides_count_url)

        assert response.status_code == 200
        assert "upcoming" in response.data.keys()
        assert "not_confirmed_rides" in response.data.keys()
        assert "confirmed_rides" in response.data.keys()

    def test_confirm_ride_ok(self):
        response = self.client.patch(
            self.confirm_ride_url,
            data={"ride_id": self.ride.id},
            content_type="application/json",
        )

        assert response.status_code == 200
        assert self.user.first_name in response.data.get("details")
        assert "confirmed" in response.data.get("details")

    def test_ride_id_required_on_confirm(self):
        response = self.client.patch(self.confirm_ride_url)

        assert response.status_code == 400
        assert "This field is required." in response.data.get("ride_id")

    def test_ride_id_required_on_cancel(self):
        response = self.client.patch(self.cancel_ride_url)

        assert response.status_code == 400
        assert "This field is required." in response.data.get("ride_id")

    def test_cancel_ride_ok(self):
        response = self.client.patch(
            self.cancel_ride_url,
            data={"ride_id": self.ride.id},
            content_type="application/json",
        )

        assert response.status_code == 200
        assert self.user.first_name in response.data.get("details")
        assert "canceled" in response.data.get("details")

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
