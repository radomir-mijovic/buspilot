from rest_framework import serializers

from ..models import Driver, DriverDocument


class DriverDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Driver
        fields = [
            "id",
            "first_name",
            "last_name",
        ]


class ExpiringDocumentsSerializer(serializers.ModelSerializer):
    related_object = serializers.SlugRelatedField(
        slug_field="last_name", read_only=True, source="driver"
    )

    class Meta:
        model = DriverDocument
        fields = [
            "id",
            "document_type",
            "days_to_expire",
            "title",
            "related_object",
        ]
