from django import forms
from django.forms import ModelForm

from .models import Guide


class GuideForm(ModelForm):
    first_name = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Unesite ime",
            }
        ),
    )
    last_name = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Unesite prezime",
            }
        ),
    )

    class Meta:
        model = Guide
        fields = [
            "email",
            "first_name",
            "last_name",
            "phone_number",
            "passport_number",
        ]
