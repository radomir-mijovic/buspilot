from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from company.mixins import CompanyRequestMixin
from vehicle.models import VehicleDocument

from .serializers import ExpiringDocumentsSerializer


class ExpiringDocumentsViewSet(
    CompanyRequestMixin,
    viewsets.ReadOnlyModelViewSet,
):
    permission_classes = [IsAuthenticated]
    serializer_class = ExpiringDocumentsSerializer
    queryset = VehicleDocument.expiring.close_to_expire()

    def get_queryset(self):
        return self.queryset.filter(
            company=self.company,
        )
