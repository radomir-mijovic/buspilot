from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from ..models import Driver, DriverDocument
from .serializers import DriverDetailSerializer, ExpiringDocumentsSerializer


class DriverDetailViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = DriverDetailSerializer
    queryset = Driver.objects.all()
    permission_classes = [IsAuthenticated]

    @action(methods=["GET"], detail=False, url_path="expiring-documents")
    def expiring_documents(self, request, *args, **kwargs):
        data = DriverDocument.expiring.close_to_expire().select_related("driver")
        serializer = ExpiringDocumentsSerializer(data, many=True)
        return Response(serializer.data)
