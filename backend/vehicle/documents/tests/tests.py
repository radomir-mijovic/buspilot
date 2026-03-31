import pytest
from common.tests.fixtures import user
from django.core.files.uploadedfile import SimpleUploadedFile
from django.urls import reverse
from vehicle.documents.tests.factories import VehicleDocumentFactory
from vehicle.models import VehicleDocument
from vehicle.tests.factories import VehicleFactory


@pytest.mark.django_db
class TestVehicleDocument:
    @pytest.fixture(autouse=True)
    def setup(self, client, user):
        client.force_login(user)
        self.vehicle = VehicleFactory()
        user.company = self.vehicle.company
        user.save()
        self.vehicle_document = VehicleDocumentFactory(
            vehicle=self.vehicle,
        )
        self.upload_url = reverse(
            "vehicle:document_upload",
            kwargs={
                "vehicle_pk": self.vehicle.pk,
            },
        )
        self.delete_url = reverse(
            "vehicle:document_delete",
            kwargs={
                "pk": self.vehicle_document.pk,
            },
        )

    def test_document_created_ok(self, client):
        file = SimpleUploadedFile(
            "test_document.pdf",
            b"document content",
            content_type="application/pdf",
        )
        client.post(
            self.upload_url,
            data={
                "file": file,
                "title": "Test document",
            },
        )
        assert VehicleDocument.objects.filter(
            vehicle=self.vehicle, title="Test document"
        ).exists()

    def test_document_create_not_ok(self, client):
        client.post(
            self.upload_url,
            data={
                "file": "",
                "title": "Test document",
            },
        )
        assert not VehicleDocument.objects.filter(
            vehicle=self.vehicle, title="Test document"
        ).exists()

    def test_document_delete_ok(self, client, user):
        client.force_login(user)
        assert self.vehicle.documents.count() == 1

        client.post(self.delete_url)
        assert self.vehicle.documents.count() == 0

    def test_user_must_be_authenticated(self, client) -> None:
        client.logout()
        response = client.post(self.upload_url)
        assert response.status_code == 302
