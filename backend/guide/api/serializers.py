from rest_framework import serializers

from guide.models import Guide


class GuideSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guide
        fields = ["id", "first_name", "last_name"]
