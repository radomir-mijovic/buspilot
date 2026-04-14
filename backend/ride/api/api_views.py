from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticated

from company.mixins import CompanyRequestMixin

from ..models import Ride
from .serializers import RideCreateSerializer, RideRetrieveSerializer


class RideRetrieveViewSet(
    generics.RetrieveAPIView,
    CompanyRequestMixin,
    viewsets.GenericViewSet,
):
    serializer_class = RideRetrieveSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Ride.objects.filter(company=self.company)


class RideCreateViewSet(
    generics.CreateAPIView,
    CompanyRequestMixin,
    viewsets.GenericViewSet,
):
    serializer_class = RideCreateSerializer
    queryset = Ride.objects.all()
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(company=self.company)


class RideUpdateViewSet(
    generics.UpdateAPIView,
    CompanyRequestMixin,
    viewsets.GenericViewSet,
):
    serializer_class = RideCreateSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Ride.objects.filter(
            company=self.company,
        )
