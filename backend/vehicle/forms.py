from django.forms import ModelForm

from .models import Vehicle


class VehicleCreateForm(ModelForm):
    class Meta:
        model = Vehicle
        fields = [
            "brand",
            "chassis_number",
            "engine_number",
            "model",
            "number_of_seats",
            "year_of_production",
            "vehicle_type",
            "weight",
        ]
