import factory
from factory.django import DjangoModelFactory

from ..models import User


class UserFactory(DjangoModelFactory):
    class Meta:
        model = User

    name = factory.Faker("name")
    email = factory.Faker("email")
