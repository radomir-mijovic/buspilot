from django import forms
from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _

from common.validators import validate_expiring_at_must_be_in_the_future

from ..models import CompanyDocument


class CompanyDocumentUploadForm(ModelForm):
    expiring_at = forms.DateField(
        validators=[validate_expiring_at_must_be_in_the_future],
        widget=forms.DateInput(
            attrs={
                "class": "form-control",
                "id": "doc-expiry",
                "type": "date",
                "required": True,
            }
        ),
    )

    class Meta:
        model = CompanyDocument
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
                    "placeholder": _("Naziv dokumenta"),
                }
            ),
            "document_type": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "id": "doc-type",
                    "placeholder": _("Tip dokumenta"),
                    "required": "true",
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
