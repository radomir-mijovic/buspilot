from django import forms
from django.forms import ModelForm
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from ..models import AgencyDocument


class AgencyDocumentUploadForm(ModelForm):
    class Meta:
        model = AgencyDocument
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
                    "placeholder": "npr. Ugovor o prevozu",
                }
            ),
            "document_type": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "id": "doc-type",
                    "placeholder": "npr. Ugovor",
                }
            ),
            "expiring_at": forms.DateInput(
                attrs={
                    "class": "form-control",
                    "id": "doc-expiry",
                    "type": "date",
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
                raise forms.ValidationError(_("Date must be in the future."))

        return expiring_at
