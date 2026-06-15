from rest_framework import serializers

from vehicle.api.fields import VehicleBrandSlugRelatedField

from ..models import Defect


class ReportDefectSerializer(serializers.ModelSerializer):
    vehicle = VehicleBrandSlugRelatedField(slug_field="id")

    class Meta:
        model = Defect
        fields = ["description", "vehicle"]
