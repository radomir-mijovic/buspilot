from django import forms
from django.forms import ModelForm

from company.models import Company

from .models import Defect


class DefectForm(ModelForm):
    def __init__(self, *args, **kwargs) -> None:
        company = kwargs.pop("company", None)
        super().__init__(*args, **kwargs)
        print(company)

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
            "vehicles": forms.SelectMultiple(
                attrs={
                    "class": "form-select",
                },
            ),
        }
