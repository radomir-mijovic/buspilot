from rest_framework import serializers

from vehicle.models import VehicleDocument


class ExpiringDocumentsSerializer(serializers.ModelSerializer):
    related_object = serializers.SlugRelatedField(
        slug_field="model", read_only=True, source="vehicle"
    )

    class Meta:
        model = VehicleDocument
        fields = [
            "id",
            "document_type",
            "days_to_expire",
            "title",
            "related_object",
        ]
