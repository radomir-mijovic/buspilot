from company.models import Company
from factory.declarations import SubFactory
from factory.django import DjangoModelFactory
from factory.faker import Faker

from ..models import Guide


class GuideFactory(DjangoModelFactory):
    class Meta:
        model = Guide

    company = SubFactory(Company)
    email = Faker("email")
    first_name = Faker("name")
    last_name = Faker("name")
