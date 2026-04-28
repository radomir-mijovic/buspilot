from factory.declarations import SubFactory
from factory.django import DjangoModelFactory
from factory.faker import Faker

from company.tests.factories import CompanyFactory

from ..models import Driver


class DriverFactory(DjangoModelFactory):
    class Meta:
        model = Driver

    email = Faker("email")
    first_name = Faker("name")
    last_name = Faker("name")
    company = SubFactory(CompanyFactory)
