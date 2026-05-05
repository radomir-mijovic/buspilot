import logging

from django.db.models.signals import post_delete, post_save
from django.dispatch import receiver

from auth.models import User, UserTypeChoices
from common.utils import generate_random_password

from .models import Driver

logger = logging.getLogger(__name__)


@receiver(post_delete, sender=Driver)
def delete_related_user_account(sender, instance, **kwargs) -> None:
    try:
        User.objects.get(
            email=instance.email,
            company=instance.company,
            user_type=UserTypeChoices.DRIVER,
        ).delete()
    except User.DoesNotExist:
        logger.warning(
            f"User to delete not found for driver: {instance.email}",
        )


@receiver(post_save, sender=Driver)
def create_related_user_account(sender, instance, created, **kwargs) -> None:
    if created:
        User.objects.create_user(
            username=f"{instance.first_name.lower()}",
            password=generate_random_password(),
            email=instance.email,
            first_name=instance.first_name if instance.first_name else "",
            last_name=instance.last_name if instance.last_name else "",
            user_type=UserTypeChoices.DRIVER,
            company=instance.company,
        )
