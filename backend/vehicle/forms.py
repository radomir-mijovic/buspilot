from django import forms
from django.forms import ModelForm

from .models import Vehicle


class VehicleCreateForm(ModelForm):
    class Meta:
        model = Vehicle
        fields = [
            "brand",
            "chassis_number",
            "color",
            "engine_number",
            "horse_power",
            "licence_number",
            "model",
            "number_of_seats",
            "year_of_production",
            "vehicle_type",
            "weight",
        ]

        widgets = {
            "brand": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "id": "brand-field",
                    "placeholder": "npr. Mercedes",
                    "required": "true",
                }
            ),
            "model": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "id": "model-field",
                    "placeholder": "npr. Sprinter 412",
                    "required": "true",
                }
            ),
            "vehicle_type": forms.Select(
                attrs={
                    "class": "form-select",
                    "id": "vehicle-type-field",
                    "required": "true",
                }
            ),
            "year_of_production": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "id": "year-field",
                    "placeholder": "npr. 2022",
                }
            ),
            "number_of_seats": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "id": "seats-field",
                    "placeholder": "npr. 50 + 5",
                }
            ),
            "chassis_number": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "id": "chassis_number",
                    "placeholder": "npr. HGCM8...",
                }
            ),
            "engine_number": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "id": "engine_number",
                    "placeholder": "npr. ALF 123 456...",
                }
            ),
            "horse_power": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "id": "horse_power",
                    "placeholder": "HP",
                }
            ),
            "weight": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "id": "weight",
                    "placeholder": "npr. 3120kg",
                }
            ),
            "licence_number": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "id": "licence_number",
                    "placeholder": "npr. PG-AU352",
                }
            ),
            "color": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "id": "color",
                    "placeholder": "npr. Svijetlo plava",
                }
            ),
        }
