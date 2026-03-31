import pytest
from auth.models import User
from company.tests.factories import CompanyFactory
from django.urls import reverse

from ..models import Vehicle
from .factories import VehicleFactory


@pytest.fixture
def user(db):
    return User.objects.create_user(
        username="testuser",
        password="strongpassword",
    )


@pytest.mark.django_db
class TestVehicle:
    @pytest.fixture(autouse=True)
    def setup(self, user):
        self.company = CompanyFactory()
        user.company = self.company
        user.save()
        self.vehicle = VehicleFactory(company=self.company)

    def test_return_list_ok(self, client, user):
        client.force_login(user)
        response = client.get(reverse("vehicle:vehicles"))
        assert str(self.vehicle.brand) in response.text
        assert response.status_code == 200

    def test_not_return_other_user_company_vehicle(self, client):
        new_user = User.objects.create_user(
            username="newuser",
            password="strongpassword",
        )
        new_user.refresh_from_db()
        client.force_login(new_user)
        response = client.get(reverse("vehicle:vehicles"))
        assert str(self.vehicle.brand) not in response.text

    def test_create_vehicle_ok(self, client, user):
        client.force_login(user)
        response = client.post(
            reverse("vehicle:vehicles_create"),
            {"brand": "Mercedes", "model": "Sprinter"},
        )
        assert response.status_code == 302
        assert Vehicle.objects.filter(brand="Mercedes", company=self.company).exists()

    def test_create_vehicle_missing_brand(self, client, user):
        client.force_login(user)
        response = client.post(
            reverse("vehicle:vehicles_create"),
            {"model": "Sprinter"},
        )
        assert response.status_code == 302
        assert not Vehicle.objects.filter(
            model="Sprinter", company=self.company
        ).exists()

    def test_create_vehicle_missing_model(self, client, user):
        client.force_login(user)
        response = client.post(
            reverse("vehicle:vehicles_create"),
            {"brand": "Mercedes"},
        )
        assert response.status_code == 302
        assert not Vehicle.objects.filter(
            brand="Mercedes", company=self.company
        ).exists()

    def test_create_vehicle_missing_all_required_fields(self, client, user):
        client.force_login(user)
        vehicle_count = Vehicle.objects.filter(company=self.company).count()
        response = client.post(reverse("vehicle:vehicles_create"), {})
        assert response.status_code == 302
        assert Vehicle.objects.filter(company=self.company).count() == vehicle_count

    def test_update_vehicle_ok(self, client, user):
        client.force_login(user)
        response = client.post(
            reverse("vehicle:vehicles_update", kwargs={"pk": self.vehicle.pk}),
            {"brand": "Volvo", "model": "9700"},
        )
        assert response.status_code == 302
        self.vehicle.refresh_from_db()
        assert self.vehicle.brand == "Volvo"
        assert self.vehicle.model == "9700"

    def test_update_vehicle_missing_brand(self, client, user):
        client.force_login(user)
        original_brand = self.vehicle.brand
        response = client.post(
            reverse("vehicle:vehicles_update", kwargs={"pk": self.vehicle.pk}),
            {"model": "9700"},
        )
        assert response.status_code == 302
        self.vehicle.refresh_from_db()
        assert self.vehicle.brand == original_brand

    def test_update_vehicle_missing_model(self, client, user):
        client.force_login(user)
        original_model = self.vehicle.model
        response = client.post(
            reverse("vehicle:vehicles_update", kwargs={"pk": self.vehicle.pk}),
            {"brand": "Volvo"},
        )
        assert response.status_code == 302
        self.vehicle.refresh_from_db()
        assert self.vehicle.model == original_model

    def test_update_vehicle_missing_all_required_fields(self, client, user):
        client.force_login(user)
        original_brand = self.vehicle.brand
        original_model = self.vehicle.model
        response = client.post(
            reverse("vehicle:vehicles_update", kwargs={"pk": self.vehicle.pk}),
            {},
        )
        assert response.status_code == 302
        self.vehicle.refresh_from_db()
        assert self.vehicle.brand == original_brand
        assert self.vehicle.model == original_model

    def test_user_must_be_authenticated(self, client) -> None:
        response = client.get(reverse("vehicle:vehicles"))
        assert response.status_code == 302
