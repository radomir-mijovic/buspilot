from rest_framework import serializers

from ride.models import Ride

from ..models import Driver, DriverDocument


class DriverDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Driver
        fields = [
            "id",
            "first_name",
            "last_name",
        ]


class ExpiringDocumentsSerializer(serializers.ModelSerializer):
    related_object = serializers.SlugRelatedField(
        slug_field="last_name", read_only=True, source="driver"
    )

    class Meta:
        model = DriverDocument
        fields = [
            "id",
            "document_type",
            "days_to_expire",
            "title",
            "related_object",
        ]


class DriverRidesSerializer(serializers.ModelSerializer):
    agency = serializers.SlugRelatedField(
        slug_field="name",
        read_only=True,
    )
    ride_type = serializers.SerializerMethodField()
    start_date = serializers.DateField(format="%d.%m.%y")
    start_time = serializers.TimeField(format="%H:%M")
    is_confirmed = serializers.SerializerMethodField()

    def get_is_confirmed(self, obj):
        driver = self.context["request"].user
        return driver in obj.confirmed_by.all()

    def get_ride_type(self, obj):
        return obj.get_ride_type_display()

    class Meta:
        model = Ride
        fields = [
            "id",
            "agency",
            "is_confirmed",
            "start_date",
            "start_time",
            "start_location",
            "title",
            "ride_type",
        ]


class GetRideSerializer(serializers.Serializer):
    ride_id = serializers.IntegerField(required=True)
