from company.tests.factories import CompanyFactory
from factory.declarations import SubFactory
from factory.django import DjangoModelFactory
from factory.faker import Faker

from ..models import Vehicle


class VehicleFactory(DjangoModelFactory):
    class Meta:
        model = Vehicle

    brand = Faker("company")
    model = Faker("name")
    company = SubFactory(CompanyFactory)
