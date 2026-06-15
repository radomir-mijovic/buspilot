from django.utils.translation import gettext_lazy as _
from django_countries.fields import CountryField
from django_countries.serializers import CountryFieldMixin
from rest_framework import serializers

from ..models import RequestDemo


class RequestDemoSerializer(CountryFieldMixin, serializers.ModelSerializer):
    email = serializers.EmailField()
    country = CountryField()

    class Meta:
        model = RequestDemo
        fields = ["company", "country", "contact_number", "email"]

    def validate_email(self, value):
        if RequestDemo.objects.filter(email__iexact=value.lower()):
            raise serializers.ValidationError(
                _("This email has already submited request for demo."),
            )
        return value
