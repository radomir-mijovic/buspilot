from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from . import constants


class UserTypeChoices(models.IntegerChoices):
    ADMIN = constants.ADMIN, "Admin"
    DRIVER = constants.DRIVER, "Driver"


class User(AbstractUser):
    email = models.EmailField(_("email address"), blank=True, unique=True)
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
