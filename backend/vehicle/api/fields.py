from rest_framework import serializers

from ..models import Vehicle


class VehicleBrandSlugRelatedField(serializers.SlugRelatedField):
    def get_queryset(self):
        company = self.context["request"].user.company
        return Vehicle.objects.filter(company=company)
