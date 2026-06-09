from django.shortcuts import get_object_or_404
from django.utils.translation import gettext_lazy as _
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from auth.permissions import AdminPermission
from defect.api.serializers import ReportDefectSerializer
from ride.models import Ride
from vehicle.api.serializers import VehicleDetailSerializer
from vehicle.models import Vehicle

from ..models import Driver, DriverDocument
from .permissions import BaseUserDriverPermission
from .serializers import (
    DriverDetailSerializer,
    DriverRidesSerializer,
    ExpiringDocumentsSerializer,
    GetRideSerializer,
    PassRideSerializer,
)


class DriverDetailViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = DriverDetailSerializer
    queryset = Driver.objects.all()
    permission_classes = [IsAuthenticated, AdminPermission]

    @action(methods=["GET"], detail=False, url_path="expiring-documents")
    def expiring_documents(self, request, *args, **kwargs):
        data = DriverDocument.expiring.close_to_expire().select_related("driver")
        serializer = ExpiringDocumentsSerializer(data, many=True)
        return Response(serializer.data)


class DriverPortalViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = DriverRidesSerializer
    permission_classes = [BaseUserDriverPermission]

    def get_queryset(self):
        qs = self.driver.rides_from_today_and_on.select_related(
            "agency",
        ).prefetch_related("guides")

        if start_date := self.request.query_params.get("start_date"):
            return qs.filter(start_date=start_date)

        return qs

    @property
    def driver(self) -> Driver:
        return Driver.objects.get(pk=self.request.user.pk)

    @property
    def ride(self) -> Ride:
        serializer = GetRideSerializer(data=self.request.data)
        serializer.is_valid(raise_exception=True)
        return get_object_or_404(
            self.driver.drivers_rides,
            id=serializer.validated_data["ride_id"],
        )

    @action(methods=["GET"], detail=False, url_path="driver-details")
    def driver_details(self, request, *args, **kwargs):
        driver = self.request.user
        serializer = DriverDetailSerializer(driver)
        return Response(serializer.data)

    @action(methods=["GET"], detail=False, url_path="defect-vehicles")
    def defect_vehicles(self, request, *args, **kwargs):
        vehicles = Vehicle.objects.filter(company=self.driver.company)
        serializer = VehicleDetailSerializer(vehicles, many=True)
        return Response(serializer.data)

    @action(methods=["POST"], detail=False, url_path="report-defects")
    def report_defects(self, request, *args, **kwargs):
        print(request.data)
        serializer = ReportDefectSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(company=self.driver.company, reported_by=self.driver)
        return Response(serializer.data)

    @action(methods=["GET"], detail=False, url_path="rides-count")
    def rides_count(self, request, *args, **kwargs):
        return Response(
            {
                "upcoming": self.driver.rides_from_today_and_on.count(),
                "not_confirmed_rides": self.driver.rides_not_confirmed.count(),
                "confirmed_rides": self.driver.rides_confirmed.count(),
            }
        )

    @action(methods=["PATCH"], detail=False, url_path="confirm-ride")
    def confirm_ride(self, request, *args, **kwargs):
        self.ride.confirmed_by.add(self.driver)
        return Response({"details": _(f"{self.ride} confirmed")})

    @action(methods=["PATCH"], detail=False, url_path="cancel-ride")
    def cancel_ride(self, request, *args, **kwargs):
        self.ride.confirmed_by.remove(self.driver)
        return Response({"details": _(f"{self.ride} canceled")})

    @action(methods=["GET"], detail=False, url_path="pass-rides")
    def pass_rides(self, request, *args, **kwargs):
        qs = self.driver.pass_rides.select_related("agency")
        if filter_date := request.query_params.get("filter_date"):
            qs = qs.filter(start_date=filter_date)

        serializer = PassRideSerializer(
            qs,
            context={"request": request},
            many=True,
        )
        return Response(serializer.data)
