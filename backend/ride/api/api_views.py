import calendar
from datetime import date
from typing import Iterable

from django.db import models
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
    queryset = Ride.objects.all()

    def filter_queryset(self, queryset):
        month, year, ride_type = self.get_query_params()

        if month and year:
            queryset = self.filter_by_date(queryset, month=month, year=year)

        if ride_type:
            queryset = queryset.filter(ride_type=ride_type)

        return queryset.filter(
            company=self.company,
        ).select_related("agency")

    def filter_by_date(self, qs, *, month, year) -> models.QuerySet[Ride]:
        month = int(month)
        year = int(year)

        last_day = calendar.monthrange(year, month)[1]
        first_of_month = date(year, month, 1)
        last_of_month = date(year, month, last_day)

        qs = qs.filter(
            start_date__lte=last_of_month,
            end_date__gte=first_of_month,
        )
        return qs

    def get_query_params(self) -> Iterable[str]:
        month = self.request.query_params.get("month")
        year = self.request.query_params.get("year")
        ride_type = self.request.query_params.get("type")
        return month, year, ride_type

    def perform_create(self, serializer):
        serializer.save(company=self.company)

    def get_serializer_class(self):
        if self.action in ["create", "update", "partial_update"]:
            return RideCreateSerializer
        return self.serializer_class
