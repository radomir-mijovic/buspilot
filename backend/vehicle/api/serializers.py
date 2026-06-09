from rest_framework import serializers

from ..models import Vehicle, VehicleDocument


class VehicleDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = [
            "id",
            "brand",
            "licence_number",
            "model",
        ]


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

