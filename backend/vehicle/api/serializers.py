from rest_framework import serializers

from ..models import Vehicle


class VehicleDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = [
            "id",
            "brand",
            "model",
        ]
