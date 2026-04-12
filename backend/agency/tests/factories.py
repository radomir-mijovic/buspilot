from factory.declarations import SubFactory
from factory.django import DjangoModelFactory
from factory.faker import Faker

from company.tests.factories import CompanyFactory

from ..models import Agency


class AgencyFactory(DjangoModelFactory):
    class Meta:
        model = Agency

    ceo = Faker("name")
    city = Faker("name")
    company = SubFactory(CompanyFactory)
    name = Faker("name")
