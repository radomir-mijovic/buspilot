from factory.declarations import SubFactory
from factory.django import DjangoModelFactory
from factory.faker import Faker

from driver.models import DriverDocument
from driver.tests.factories import DriverFactory


class DriverDocumentFactory(DjangoModelFactory):
    class Meta:
        model = DriverDocument

    title = Faker("name")
    document_type = Faker("name")
    expiring_at = Faker("date_object")
    driver = SubFactory(DriverFactory)
