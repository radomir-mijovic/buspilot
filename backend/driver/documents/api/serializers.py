from rest_framework import serializers

from driver.models import DriverDocument


class ExpiringDocumentsSerializer(serializers.ModelSerializer):
    vehicle = serializers.SlugRelatedField(
        slug_field="model",
        read_only=True,
    )

    class Meta:
        model = DriverDocument
        fields = ["id", "document_type", "days_to_expire", "vehicle"]
