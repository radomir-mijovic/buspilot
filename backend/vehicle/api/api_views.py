from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from ride.api.serializers import RideCalendarSerializer

from ..models import Vehicle
from .serializers import VehicleDetailSerializer


class VehicleDetailViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = VehicleDetailSerializer
    queryset = Vehicle.objects.all()
    permission_classes = [IsAuthenticated]

    @action(methods=["GET"], detail=True, url_path="calendar-events")
    def calendar_events(self, request, *args, **kwargs):
        vehicle = self.get_object()
        serializer = RideCalendarSerializer(vehicle.rides.all(), many=True)
        return Response(serializer.data)
