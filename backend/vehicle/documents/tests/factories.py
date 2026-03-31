from factory.declarations import SubFactory
from factory.django import DjangoModelFactory
from factory.faker import Faker

from vehicle.models import VehicleDocument
from vehicle.tests.factories import VehicleFactory


class VehicleDocumentFactory(DjangoModelFactory):
    class Meta:
        model = VehicleDocument

    title = Faker("name")
    document_type = Faker("name")
    expiring_at = Faker("date_object")
    vehicle = SubFactory(VehicleFactory)
