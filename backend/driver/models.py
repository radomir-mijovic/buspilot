from django.core.validators import FileExtensionValidator
from django.db import models

from common.models import VALID_FILE_EXTENSIONS, DocumentAbstract, PersonAbstract


class Driver(PersonAbstract):
    pass


class DriverDocument(DocumentAbstract):
    file = models.FileField(
        upload_to="drivers/documents",
        validators=[
            FileExtensionValidator(
                allowed_extensions=VALID_FILE_EXTENSIONS,
            ),
        ],
    )

    driver = models.ForeignKey(
        Driver,
        on_delete=models.CASCADE,
        blank=True,
        related_name="documents",
    )
