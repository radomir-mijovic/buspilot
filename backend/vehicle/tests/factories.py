import factory
from factory.django import DjangoModelFactory

from company.tests.factories import CompanyFactory

from ..models import Vehicle


class VehicleFactory(DjangoModelFactory):
    class Meta:
        model = Vehicle

    brand = factory.Faker("company")
    model = factory.Faker("name")
    company = factory.SubFactory(CompanyFactory)
