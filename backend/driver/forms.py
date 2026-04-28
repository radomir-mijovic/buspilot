from django import forms
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

        widgets = {
            "email": forms.EmailInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Unesite email",
                    "required": "true",
                }
            ),
            "first_name": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Unesite ime",
                    "required": "true",
                }
            ),
            "last_name": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Unesite prezime",
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
