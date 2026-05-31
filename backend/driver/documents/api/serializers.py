from rest_framework import serializers

from driver.models import DriverDocument


class ExpiringDocumentsSerializer(serializers.ModelSerializer):
    related_object = serializers.SlugRelatedField(
        slug_field="last_name",
        read_only=True,
        source="driver",
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
