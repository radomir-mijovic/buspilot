import pytest
from django.urls import reverse
from django.utils import timezone
from parameterized import parameterized

from common.tests.fixtures import user  # noqa: F401, F811
from company.tests.factories import CompanyFactory
from driver.tests.factories import DriverFactory
from guide.tests.factories import GuideFactory
from ride.forms import RideForm
from vehicle.tests.factories import VehicleFactory

from .factories import RideFactory


@pytest.mark.django_db
class TestRides:
    @pytest.fixture(autouse=True)
    def setup(self, client, user):
        client.force_login(user)
        self.client = client
        self.company = CompanyFactory()
        user.company = self.company
        user.save()
        self.ride = RideFactory(title="Test Ride", company=self.company)

        self.list_url = reverse("ride:ride_list")
        self.create_url = reverse("ride:ride_create")
        self.update_url = reverse(
            "ride:ride_update",
            kwargs={"pk": self.ride.pk},
        )
        self.delete_url = reverse(
            "ride:ride_delete",
            kwargs={"pk": self.ride.pk},
        )

    def test_return_list_ok(self, client):
        response = client.get(self.list_url)
        assert self.ride.title in response.text

    def test_list_filter_ok(self, client):
        other_company = CompanyFactory()
        other_ride = RideFactory(company=other_company)
        response = client.get(self.list_url)
        assert other_ride.title not in response.text

    def test_create_ride_ok(self, client):
        assert self.company.rides.count() == 1
        client.post(
            self.create_url,
            {
                "title": "New Ride",
                "description": "Description",
                "ride_type": 2,
                "start_date": timezone.now().date(),
            },
        )
        assert self.company.rides.count() == 2

    def test_create_ride_not_ok(self, client):
        assert self.company.rides.count() == 1
        client.post(self.create_url, {})
        assert self.company.rides.count() == 1

    def test_update_ride_ok(self, client):
        assert not self.ride.title == "Updated title"
        assert not self.ride.ride_type == 3

        client.post(
            self.update_url,
            {"title": "Updated title", "ride_type": 3},
        )

        self.ride.refresh_from_db()
        assert self.ride.title == "Updated title"
        assert self.ride.ride_type == 3

    def test_update_ride_not_ok(self, client):
        assert self.ride.title == "Test Ride"
        client.post(self.update_url, {})
        assert self.ride.title == "Test Ride"

    def test_delete_ride_ok(self, client) -> None:
        client.post(self.delete_url)
        assert self.company.rides.count() == 0

    def test_cant_delete_other_company_ride(self, client) -> None:
        assert self.company.rides.count() == 1

        other_company = CompanyFactory()
        other_ride = RideFactory(company=other_company)
        client.post(
            reverse(
                "ride:ride_delete",
                kwargs={"pk": other_ride.pk},
            ),
        )

        assert self.company.rides.count() == 1

    def test_form_filters_vehicle_by_company(self):
        vehicle_1 = VehicleFactory(company=self.company)
        not_company_vehicle = VehicleFactory()
        form = RideForm(company=self.company)

        assert vehicle_1 in form.fields["vehicles"].queryset
        assert not_company_vehicle not in form.fields["vehicles"].queryset

    def test_form_filters_guide_by_company(self):
        other_company = CompanyFactory()
        guide_1 = GuideFactory(company=self.company)
        not_company_guide = GuideFactory(company=other_company)
        form = RideForm(company=self.company)

        assert guide_1 in form.fields["guides"].queryset
        assert not_company_guide not in form.fields["guides"].queryset

    def test_form_filters_driver_by_company(self):
        other_company = CompanyFactory()
        driver_1 = DriverFactory(company=self.company)
        not_company_driver = DriverFactory(company=other_company)
        form = RideForm(company=self.company)

        assert driver_1 in form.fields["drivers"].queryset
        assert not_company_driver not in form.fields["drivers"].queryset

    @parameterized.expand(
        (
            ["ride:ride_list", None],
            ["ride:ride_create", None],
            ["ride:ride_delete", {"pk": 1}],
            ["ride:ride_update", {"pk": 1}],
        )
    )
    def test_user_must_be_authenticated(self, url, kwargs) -> None:
        self.client.logout()
        response = self.client.get(reverse(url, kwargs=kwargs))
        assert response.status_code == 302
