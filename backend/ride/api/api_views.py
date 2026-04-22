from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticated

from company.mixins import CompanyRequestMixin

from ..models import Ride
from .serializers import RideCreateSerializer, RideRetrieveSerializer


class RideViewSet(
    generics.ListAPIView,
    generics.RetrieveAPIView,
    generics.CreateAPIView,
    generics.UpdateAPIView,
    CompanyRequestMixin,
    viewsets.GenericViewSet,
):
    serializer_class = RideRetrieveSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        qs = Ride.objects.filter(company=self.company).select_related("agency")
        month = self.request.query_params.get("month")
        year = self.request.query_params.get("year")
        ride_type = self.request.query_params.get("type")

        if month or year:
            qs = qs.filter(
                start_date__month=month,
                start_date__year=year,
            )

        if ride_type:
            qs = qs.filter(ride_type=ride_type)

        return qs

    def perform_create(self, serializer):
        serializer.save(company=self.company)

    def get_serializer_class(self):
        if self.action in ["create", "update", "partial_update"]:
            return RideCreateSerializer
        return self.serializer_class
