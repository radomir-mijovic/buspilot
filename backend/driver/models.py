from typing import Any

from django.contrib.auth.models import UserManager
from django.core.validators import FileExtensionValidator
from django.db import models

from auth.models import User, UserTypeChoices
from common.models import VALID_FILE_EXTENSIONS, DocumentAbstract
from ride.models import Ride


class DriverManager(UserManager):
    def get_queryset(self) -> models.QuerySet[Any]:
        return super().get_queryset().filter(user_type=UserTypeChoices.DRIVER)


class Driver(User):
    objects = DriverManager()

    class Meta:
        proxy = True

    def set_password(self, raw_password: str | None) -> None:
        self.raw_password = raw_password
        return super().set_password(self.raw_password)

    @property
    def from_today_and_on_rides(self):
        return Ride.rides.from_today_and_on().filter(
            company=self.company,
            drivers=self,
        )


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
