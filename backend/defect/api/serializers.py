from rest_framework import serializers

from ..models import Defect


class ReportDefectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Defect
        fields = ["description", "vehicle"]
