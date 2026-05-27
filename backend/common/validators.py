from django import forms
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


def validate_expiring_at_must_be_in_the_future(value):
    if value < timezone.now().date():
        raise forms.ValidationError(_("Date must be in the future."))

    return value
