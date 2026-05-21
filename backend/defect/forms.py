from django import forms
from django.forms import ModelForm

from .models import Defect


class DefectForm(ModelForm):
    def __init__(self, *args, **kwargs) -> None:
        company = kwargs.pop("company", None)
        super().__init__(*args, **kwargs)

        if company:
            self.fields["vehicle"].queryset = self.fields["vehicle"].queryset.filter(
                company=company
            )

    class Meta:
        model = Defect
        fields = ["description", "vehicle"]

        widgets = {
            "description": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "required": "true",
                    "rows": "3",
                }
            ),
            "vehicle": forms.Select(
                attrs={
                    "class": "form-select",
                    "id": "defectVehicle",
                    "required": "true",
                },
            ),
        }
