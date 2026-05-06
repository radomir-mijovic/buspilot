import logging

from django.db.models.signals import post_save
from django.dispatch import receiver

from common.utils import generate_random_password

from .models import Guide

logger = logging.getLogger(__name__)


@receiver(post_save, sender=Guide)
def generate_username_and_password_on_create(
    sender, instance, created, **kwargs
) -> None:
    if created:
        password = generate_random_password()
        instance.username = generate_unique_username(instance)
        instance.set_password(password)
        instance.raw_password = password
        instance.save()


def generate_unique_username(instance: Guide) -> str:
    return f"{instance.pk}_{instance.first_name.lower()}_{instance.last_name.lower()}"
