from django.forms import ModelForm

from .models import Driver


class DriverForm(ModelForm):
    class Meta:
        model = Driver
        fields = [
            "email",
            "first_name",
            "last_name",
            "phone_number",
            "passport_number",
        ]
