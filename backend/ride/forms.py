from django import forms

from .models import Ride


class RideForm(forms.ModelForm):
    class Meta:
        model = Ride
        fields = "__all__"
        exclude = ["company"]

        widgets = {
            "title": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "id": "title",
                }
            ),
            "start_location": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "id": "start_location",
                }
            ),
            "end_location": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "id": "end_location",
                }
            ),
            "description": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "id": "description",
                    "rows": 5,
                }
            ),
            "ride_type": forms.Select(
                attrs={
                    "class": "form-select",
                    "id": "FormInputState",
                    "data-choices": "",
                    "data-choices-sorting": "true",
                    "required": "true",
                }
            ),
            "start_time": forms.TimeInput(
                attrs={
                    "class": "form-control",
                    "type": "time",
                    "step": "60",
                    "id": "start_time",
                    "placeholder": "HH:MM",
                }
            ),
            "end_time": forms.TimeInput(
                attrs={
                    "class": "form-control",
                    "type": "time",
                    "step": "60",
                    "id": "end_time",
                    "placeholder": "HH:MM",
                }
            ),
            "start_date": forms.DateInput(
                attrs={
                    "class": "form-control",
                    "type": "date",
                    "id": "start_date",
                    "placeholder": "YYYY-MM-DD",
                }
            ),
            "end_date": forms.DateInput(
                attrs={
                    "class": "form-control",
                    "type": "date",
                    "id": "end_date",
                    "placeholder": "YYYY-MM-DD",
                }
            ),
            "is_all_day": forms.CheckboxInput(
                attrs={
                    "class": "form-check-input",
                    "id": "is_all_day",
                    "role": "switch",
                }
            ),
            "vehicles": forms.SelectMultiple(
                attrs={
                    "class": "form-select",
                },
            ),
            "drivers": forms.SelectMultiple(
                attrs={
                    "class": "form-select",
                },
            ),
        }
