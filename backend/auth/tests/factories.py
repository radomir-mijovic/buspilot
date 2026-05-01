import factory
from factory.django import DjangoModelFactory

from ..models import User


class UserFactory(DjangoModelFactory):
    class Meta:
        model = User

    first_name = factory.Faker("name")
    last_name = factory.Faker("name")
    email = factory.Faker("email")
