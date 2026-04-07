from company.tests.factories import CompanyFactory
from factory.declarations import SubFactory
from factory.django import DjangoModelFactory
from factory.faker import Faker

from ..models import Vehicle
from .. import constants


class VehicleFactory(DjangoModelFactory):
    class Meta:
        model = Vehicle

    brand = Faker("company")
    model = Faker("name")
    vehicle_type = constants.BUS
    company = SubFactory(CompanyFactory)
