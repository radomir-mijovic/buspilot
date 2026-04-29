from django import forms
from django.forms import ModelForm
from django.utils import timezone

from ..models import VehicleDocument


class VehicleDocumentUploadForm(ModelForm):
    class Meta:
        model = VehicleDocument
        fields = [
            "title",
            "document_type",
            "expiring_at",
            "file",
        ]
        widgets = {
            "title": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "id": "doc-title",
                    "required": "true",
                    "placeholder": "npr. Saobraćajna dozvola",
                }
            ),
            "document_type": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "id": "doc-type",
                    "placeholder": "npr. Registracija",
                }
            ),
            "expiring_at": forms.DateInput(
                attrs={
                    "class": "form-control",
                    "id": "doc-expiry",
                    "type": "date",
                    "placeholder": "npr. Registracija",
                }
            ),
            "file": forms.FileInput(
                attrs={
                    "class": "form-control",
                    "id": "doc-file",
                    "required": "true",
                    "type": "file",
                }
            ),
        }

    def clean_expiring_at(self):
        if expiring_at := self.cleaned_data["expiring_at"]:
            if expiring_at < timezone.now().date():
                raise forms.ValidationError("Date must be in the future.")

        return expiring_at
