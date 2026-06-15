from django.utils.translation import gettext_lazy as _
from django_countries import countries
from rest_framework.response import Response
from rest_framework.views import APIView

from requestdemo.const import ALLOWED_COUNTRIES

from .serializers import RequestDemoSerializer


class RequestDemoApiView(APIView):
    authentication_classes = []
    serializer_class = RequestDemoSerializer
    permission_classes = []

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(
            {
                "details": _(
                    """You have successfully submited request."""
                    """ Someone from our team will reach to you in next 24 hours."""
                )
            }
        )

    def options(self, request, *args, **kwargs):
        data = [{"name": name} for name in countries if name[0] in ALLOWED_COUNTRIES]
        return Response(data)
