from django import forms

from .models import Agency


class AgencyCreateForm(forms.ModelForm):
    class Meta:
        model = Agency
        fields = "__all__"
        exclude = [
            "company",
            "card_header_color",
        ]
        widgets = {
            "name": forms.TextInput(
                attrs={
                    "class": "form-control",
                },
            ),
            "city": forms.TextInput(
                attrs={
                    "class": "form-control",
                },
            ),
            "phone_number": forms.TextInput(
                attrs={
                    "class": "form-control",
                },
            ),
            "mobile_phone_number": forms.TextInput(
                attrs={
                    "class": "form-control",
                },
            ),
            "ceo": forms.TextInput(
                attrs={
                    "class": "form-control",
                },
            ),
            "contact_person": forms.TextInput(
                attrs={
                    "class": "form-control",
                },
            ),
            "country": forms.Select(
                attrs={
                    "class": "form-control",
                },
            ),
        }
