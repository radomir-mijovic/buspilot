from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    company = models.ForeignKey(
        "company.Company",
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        related_name="users",
    )
