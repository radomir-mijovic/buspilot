from django import forms

from .models import Ride


class RideForm(forms.ModelForm):
    def __init__(self, *args, **kwargs) -> None:
        company = kwargs.pop("company", None)
        super().__init__(*args, **kwargs)

        for field in ["vehicles", "drivers", "guides"]:
            self.fields[field].queryset = self.fields[field].queryset.filter(
                company=company,
            )

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
                    "rows": 3,
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
                    "placeholder": "DD-MM-YYYY",
                    "required": "true",
                }
            ),
            "end_date": forms.DateInput(
                attrs={
                    "class": "form-control",
                    "type": "date",
                    "id": "end_date",
                    "placeholder": "DD-MM-YYYY",
                    "required": "true",
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
            "guides": forms.SelectMultiple(
                attrs={
                    "class": "form-select",
                },
            ),
            "agency": forms.Select(
                attrs={
                    "class": "form-select",
                },
            ),
        }


class RideCalendarVehicleForm(forms.ModelForm):
    def __init__(self, *args, **kwargs) -> None:
        company = kwargs.pop("company", None)
        super().__init__(*args, **kwargs)

        for field in ["drivers", "guides"]:
            self.fields[field].queryset = self.fields[field].queryset.filter(
                company=company,
            )

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
                    "rows": 3,
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
                    "required": "true",
                }
            ),
            "end_date": forms.DateInput(
                attrs={
                    "class": "form-control",
                    "type": "date",
                    "id": "end_date",
                    "placeholder": "YYYY-MM-DD",
                    "required": "true",
                }
            ),
            "is_all_day": forms.CheckboxInput(
                attrs={
                    "class": "form-check-input",
                    "id": "is_all_day",
                    "role": "switch",
                }
            ),
            # "vehicles": forms.SelectMultiple(
            #    attrs={
            #        "class": "form-select",
            #    },
            # ),
            "drivers": forms.SelectMultiple(
                attrs={
                    "class": "form-select",
                },
            ),
            "guides": forms.SelectMultiple(
                attrs={
                    "class": "form-select",
                },
            ),
            "agency": forms.Select(
                attrs={
                    "class": "form-select",
                },
            ),
        }
