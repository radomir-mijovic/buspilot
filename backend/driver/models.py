from typing import Any

from django.contrib.auth.models import UserManager
from django.core.validators import FileExtensionValidator
from django.db import models
from django.utils import timezone

from auth.models import User, UserTypeChoices
from common.models import VALID_FILE_EXTENSIONS, DocumentAbstract


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
    def rides_from_today_and_on(self):
        return self.drivers_rides.filter(
            start_date__gte=timezone.now().date(),
        ).order_by("start_date", "start_time")

    @property
    def pass_rides(self):
        return self.drivers_rides.filter(
            start_date__lt=timezone.now().date()
        ).order_by("-start_date", "-start_time")

    @property
    def rides_confirmed(self):
        return self.rides_from_today_and_on.filter(
            confirmed_by=self,
        )

    @property
    def rides_not_confirmed(self):
        return self.rides_from_today_and_on.exclude(
            confirmed_by=self,
        ).distinct()


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
