from django import forms
from django.forms import ModelForm

from .models import Driver


class DriverForm(ModelForm):
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
        model = Driver
        fields = [
            "email",
            "first_name",
            "last_name",
            "phone_number",
            "passport_number",
        ]

        widgets = {
            "email": forms.EmailInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Unesite email",
                    "required": "true",
                }
            ),
            "phone_number": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Nrp: +38267...",
                }
            ),
            "passport_number": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Nrp: I932J...",
                }
            ),
        }
