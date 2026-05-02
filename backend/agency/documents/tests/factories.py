from factory.declarations import SubFactory
from factory.django import DjangoModelFactory
from factory.faker import Faker

from agency.models import AgencyDocument
from agency.tests.factories import AgencyFactory


class AgencyDocumentFactory(DjangoModelFactory):
    class Meta:
        model = AgencyDocument

    title = Faker("name")
    document_type = Faker("name")
    expiring_at = Faker("date_object")
    agency = SubFactory(AgencyFactory)
