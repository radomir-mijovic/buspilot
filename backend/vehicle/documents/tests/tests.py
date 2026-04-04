import pytest
from django.core.files.uploadedfile import SimpleUploadedFile
from django.urls import reverse
from parameterized import parameterized

from common.tests.fixtures import user
from vehicle.documents.tests.factories import VehicleDocumentFactory
from vehicle.models import VehicleDocument
from vehicle.tests.factories import VehicleFactory


@pytest.mark.django_db
class TestVehicleDocument:
    @pytest.fixture(autouse=True)
    def setup(self, client, user):
        client.force_login(user)
        self.client = client
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

    def test_document_created_ok(self, client) -> None:
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

    def test_invalid_format(self, client) -> None:
        file = SimpleUploadedFile(
            "test_document.xmlx",
            b"document content",
            content_type="application/pdf",
        )
        response = client.post(
            self.upload_url,
            data={
                "file": file,
                "title": "Test document",
            },
        )
        assert response.status_code == 302

    def test_invalid_format_htmx(self, client) -> None:
        file = SimpleUploadedFile(
            "test_document.exe",
            b"document content",
            content_type="application/pdf",
        )
        headers = {"HTTP_HX_REQUEST": "true"}
        response = client.post(
            self.upload_url,
            data={
                "file": file,
                "title": "Test document",
            },
            **headers,
        )
        assert "File extension “exe” is not allowed." in response.text
        assert response.status_code == 422

    def test_document_create_not_ok(self, client) -> None:
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

    def test_document_delete_ok(self, client, user) -> None:
        client.force_login(user)
        assert self.vehicle.documents.count() == 1

        client.post(self.delete_url)
        assert self.vehicle.documents.count() == 0

    @parameterized.expand(
        (
            ["vehicle:document_delete", {"pk": 1}],
            ["vehicle:document_upload", {"vehicle_pk": 1}],
        )
    )
    def test_user_must_be_authenticated(self, url, kwargs) -> None:
        self.client.logout()
        response = self.client.post(reverse(url, kwargs=kwargs))
        assert response.status_code == 302
