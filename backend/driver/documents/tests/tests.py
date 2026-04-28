from datetime import timedelta

import pytest
from django.core.files.uploadedfile import SimpleUploadedFile
from django.urls import reverse
from django.utils import timezone
from parameterized import parameterized

from common.tests.fixtures import user
from driver.documents.tests.factories import DriverDocumentFactory
from driver.models import DriverDocument
from driver.tests.factories import DriverFactory


@pytest.mark.django_db
class TestDriverDocument:
    @pytest.fixture(autouse=True)
    def setup(self, client, user):
        client.force_login(user)
        self.client = client
        self.driver = DriverFactory()
        user.company = self.driver.company
        user.save()
        self.driver_document = DriverDocumentFactory(
            driver=self.driver,
        )
        self.upload_url = reverse(
            "driver:document_upload",
            kwargs={
                "driver_pk": self.driver.pk,
            },
        )
        self.delete_url = reverse(
            "driver:document_delete",
            kwargs={
                "pk": self.driver_document.pk,
                "driver_pk": self.driver.pk,
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
        assert DriverDocument.objects.filter(
            driver=self.driver, title="Test document"
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

    def test_expiring_at_in_past_not_allowed(self, client):
        past_date = timezone.now().date() - timedelta(days=1)

        response = client.post(
            self.upload_url,
            data={
                "file": SimpleUploadedFile(
                    "test_document.pdf",
                    b"document content",
                    content_type="application/pdf",
                ),
                "title": "Test document",
                "expiring_at": past_date,
            },
        )

        assert "Date must be in the future" in response.context.get("errors")[0]

    def test_document_create_not_ok(self, client) -> None:
        client.post(
            self.upload_url,
            data={
                "file": "",
                "title": "Test document",
            },
        )
        assert not DriverDocument.objects.filter(
            driver=self.driver, title="Test document"
        ).exists()

    def test_document_delete_ok(self, client, user) -> None:
        client.force_login(user)
        assert self.driver.documents.count() == 1

        client.post(self.delete_url)
        assert self.driver.documents.count() == 0

    @parameterized.expand(
        (
            ["driver:document_delete", {"pk": 1, "driver_pk": 1}],
            ["driver:document_upload", {"driver_pk": 1}],
        )
    )
    def test_user_must_be_authenticated(self, url, kwargs) -> None:
        self.client.logout()
        response = self.client.post(reverse(url, kwargs=kwargs))
        assert response.status_code == 302
