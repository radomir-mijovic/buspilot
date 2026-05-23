from factory.declarations import SubFactory
from factory.django import DjangoModelFactory
from factory.faker import Faker

from company.tests.factories import CompanyFactory

from ..models import Defect


class DefectFactory(DjangoModelFactory):
    class Meta:
        model = Defect

    company = SubFactory(CompanyFactory)
    description = Faker("name")
    is_fixed = Faker("boolean")
