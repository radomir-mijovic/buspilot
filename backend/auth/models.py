from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from . import constants


class UserTypeChoices(models.IntegerChoices):
    ADMIN = constants.ADMIN, "Admin"
    DRIVER = constants.DRIVER, "Driver"
    GUIDE = constants.GUIDE, "Guide"


class User(AbstractUser):
    company = models.ForeignKey(
        "company.Company",
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        related_name="users",
    )
    user_type = models.PositiveIntegerField(
        choices=UserTypeChoices,
        default=UserTypeChoices.ADMIN,
    )
    phone_number = models.CharField(max_length=100, blank=True)
    passport_number = models.CharField(max_length=100, blank=True)
    raw_password = models.CharField(
        max_length=50,
        blank=True,
        help_text="Only storing password from read only related objects that are created by admins.",
    )

    @property
    def is_admin(self) -> bool:
        return self.user_type == UserTypeChoices.ADMIN

    @property
    def is_driver(self) -> bool:
        return self.user_type == UserTypeChoices.DRIVER

    @property
    def is_guide(self) -> bool:
        return self.user_type == UserTypeChoices.GUIDE
