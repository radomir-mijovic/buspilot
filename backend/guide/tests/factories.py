from factory.declarations import SubFactory
from factory.django import DjangoModelFactory
from factory.faker import Faker

from auth.models import UserTypeChoices
from company.models import Company

from ..models import Guide


class GuideFactory(DjangoModelFactory):
    class Meta:
        model = Guide

    company = SubFactory(Company)
    email = Faker("email")
    first_name = Faker("name")
    last_name = Faker("name")
    user_type = UserTypeChoices.GUIDE
