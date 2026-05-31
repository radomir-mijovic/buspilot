from rest_framework import serializers

from vehicle.models import VehicleDocument


class ExpiringDocumentsSerializer(serializers.ModelSerializer):
    vehicle = serializers.SlugRelatedField(
        slug_field="model",
        read_only=True,
    )

    class Meta:
        model = VehicleDocument
        fields = ["id", "document_type", "days_to_expire", "vehicle"]
