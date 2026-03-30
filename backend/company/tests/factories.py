import factory
from factory.django import DjangoModelFactory

from ..models import Company


class CompanyFactory(DjangoModelFactory):
    class Meta:
        model = Company

    name = factory.Faker("name")
    email = factory.Faker("email")
