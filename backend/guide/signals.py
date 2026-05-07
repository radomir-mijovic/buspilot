import logging

from django.db.models.signals import post_save
from django.dispatch import receiver

from common.utils import create_username, random_password

from .models import Guide

logger = logging.getLogger(__name__)


@receiver(post_save, sender=Guide)
def assign_username_and_password_on_create(
    sender,
    instance,
    created,
    **kwargs,
) -> None:
    if created:
        instance.username = create_username(instance)
        instance.set_password(random_password())
        instance.save()
