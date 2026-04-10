from django.utils import timezone
from factory import LazyFunction
from factory.declarations import SubFactory
from factory.django import DjangoModelFactory
from factory.faker import Faker

from company.models import Company

from ..models import Ride


class RideFactory(DjangoModelFactory):
    class Meta:
        model = Ride

    company = SubFactory(Company)
    description = Faker("name")
    title = Faker("name")
    ride_type = 1
    start_date = LazyFunction(lambda: timezone.now().date())
