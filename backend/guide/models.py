from typing import Any

from django.contrib.auth.models import UserManager
from django.db import models

from auth.models import User, UserTypeChoices


class GuideManager(UserManager):
    def get_queryset(self) -> models.QuerySet[Any]:
        return super().get_queryset().filter(user_type=UserTypeChoices.GUIDE)


class Guide(User):
    objects = GuideManager()

    class Meta:
        proxy = True
