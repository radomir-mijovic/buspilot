import pytest
from django.urls import reverse
from parameterized import parameterized

from auth.models import User
from auth.tests.factories import UserFactory
from company.tests.factories import CompanyFactory

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
    def setup(self, client, user):
        self.company = CompanyFactory()
        user.company = self.company
        user.save()
        self.vehicle = VehicleFactory(company=self.company)
        self.client = client
        self.client.force_login(user)
        self.user = user

    def test_return_list_ok(self):
        response = self.client.get(reverse("vehicle:vehicles"))
        assert str(self.vehicle.brand) in response.text
        assert response.status_code == 200

    def test_not_return_other_user_company_vehicle(self):
        new_user = User.objects.create_user(
            username="newuser",
            password="strongpassword",
        )
        new_user.refresh_from_db()
        self.client.force_login(new_user)
        response = self.client.get(reverse("vehicle:vehicles"))
        assert str(self.vehicle.brand) not in response.text

    def test_create_vehicle_ok(self):
        response = self.client.post(
            reverse("vehicle:vehicles_create"),
            {"brand": "Mercedes", "model": "Sprinter", "vehicle_type": 1},
        )
        assert response.status_code == 302
        assert Vehicle.objects.filter(brand="Mercedes", company=self.company).exists()

    def test_create_vehicle_missing_brand(self):
        response = self.client.post(
            reverse("vehicle:vehicles_create"),
            {"model": "Sprinter"},
        )
        assert response.status_code == 302
        assert not Vehicle.objects.filter(
            model="Sprinter", company=self.company
        ).exists()

    def test_create_vehicle_missing_model(self):
        response = self.client.post(
            reverse("vehicle:vehicles_create"),
            {"brand": "Mercedes"},
        )
        assert response.status_code == 302
        assert not Vehicle.objects.filter(
            brand="Mercedes", company=self.company
        ).exists()

    def test_create_vehicle_missing_all_required_fields(self):
        vehicle_count = Vehicle.objects.filter(company=self.company).count()
        response = self.client.post(reverse("vehicle:vehicles_create"), {})
        assert response.status_code == 302
        assert Vehicle.objects.filter(company=self.company).count() == vehicle_count

    def test_update_vehicle_ok(self):
        response = self.client.post(
            reverse("vehicle:vehicles_update", kwargs={"pk": self.vehicle.pk}),
            {"brand": "Volvo", "model": "9700", "vehicle_type": 1},
        )
        assert response.status_code == 302
        self.vehicle.refresh_from_db()
        assert self.vehicle.brand == "Volvo"
        assert self.vehicle.model == "9700"

    def test_update_vehicle_missing_brand(self):
        original_brand = self.vehicle.brand
        response = self.client.post(
            reverse("vehicle:vehicles_update", kwargs={"pk": self.vehicle.pk}),
            {"model": "9700"},
        )
        assert response.status_code == 302
        self.vehicle.refresh_from_db()
        assert self.vehicle.brand == original_brand

    def test_update_vehicle_missing_model(self,):
        original_model = self.vehicle.model
        response = self.client.post(
            reverse("vehicle:vehicles_update", kwargs={"pk": self.vehicle.pk}),
            {"brand": "Volvo"},
        )
        assert response.status_code == 302
        self.vehicle.refresh_from_db()
        assert self.vehicle.model == original_model

    def test_update_vehicle_missing_all_required_fields(self):
        original_brand = self.vehicle.brand
        original_model = self.vehicle.model
        response = self.client.post(
            reverse("vehicle:vehicles_update", kwargs={"pk": self.vehicle.pk}),
            {},
        )
        assert response.status_code == 302
        self.vehicle.refresh_from_db()
        assert self.vehicle.brand == original_brand
        assert self.vehicle.model == original_model

    @parameterized.expand(
        (
            ["vehicle:vehicles", None],
            ["vehicle:vehicles_create", None],
            ["vehicle:vehicles_delete", {"pk": 1}],
            ["vehicle:vehicles_update", {"pk": 1}],
        )
    )
    def test_user_must_be_authenticated(self, url, kwargs) -> None:
        self.client.logout()
        response = self.client.get(reverse(url, kwargs=kwargs))
        assert response.status_code == 302

    def test_delete_vehicle_ok(self):
        assert Vehicle.objects.count() == 1
        self.client.delete(
            reverse("vehicle:vehicles_delete", kwargs={"pk": self.vehicle.pk})
        )
        assert Vehicle.objects.count() == 0


    def test_update_other_company_vehicle_is_blocked(self, client):
        other_user = UserFactory()
        other_user.company = CompanyFactory()
        other_user.save()

        client.force_login(other_user)
        client.post(
            reverse("vehicle:vehicles_update", kwargs={"pk": self.vehicle.pk}),
            {"brand": "Volvo", "model": "9700", "vehicle_type": 1},
        )
        self.vehicle.refresh_from_db()
        assert not self.vehicle.model == "9700"

    def test_delete_other_company_vehicle_returns_404(self, client):
        other_user = UserFactory()
        other_user.company = CompanyFactory()
        other_user.save()

        client.force_login(other_user)

        assert Vehicle.objects.count() == 1
        self.client.delete(
            reverse("vehicle:vehicles_delete", kwargs={"pk": self.vehicle.pk})
        )
        assert Vehicle.objects.count() == 1
