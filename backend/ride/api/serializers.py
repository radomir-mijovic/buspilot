from datetime import timedelta

from rest_framework import serializers

from ride import constants

from ..models import Ride

RIDE_TYPE_CLASS = {
    constants.LINE: "bg-danger-subtle",
    constants.EXCURSION: "bg-success-subtle",
    constants.TRANSFER: "bg-info-subtle",
    constants.ROUND_TOUR: "bg-warning-subtle",
}


class RideRetrieveSerializer(serializers.ModelSerializer):
    agency = serializers.SlugRelatedField(
        slug_field="name",
        read_only=True,
    )
    class_name = serializers.SerializerMethodField()

    class Meta:
        model = Ride
        fields = [
            "id",
            "title",
            "ride_type",
            "start_date",
            "end_date",
            "start_time",
            "end_time",
            "start_location",
            "end_location",
            "agency",
            "drivers",
            "guides",
            "vehicles",
            "class_name",
        ]

    def get_class_name(self, obj):
        return RIDE_TYPE_CLASS.get(
            obj.ride_type,
            "bg-primary-subtle",
        )


class RideCalendarSerializer(serializers.ModelSerializer):
    start = serializers.DateField(source="start_date")
    end = serializers.SerializerMethodField(source="end_date")
    className = serializers.SerializerMethodField()

    class Meta:
        model = Ride
        fields = [
            "id",
            "title",
            "start",
            "end",
            "start_time",
            "end_time",
            "className",
        ]

    def get_className(self, obj):
        return RIDE_TYPE_CLASS.get(
            obj.ride_type,
            "bg-primary-subtle",
        )

    def get_end(self, obj):
        if obj.end_date:
            return obj.end_date + timedelta(days=1)
        return None


class RideCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ride
        fields = [
            "id",
            "agency",
            "drivers",
            "guides",
            "start_date",
            "end_date",
            "start_time",
            "end_time",
            "start_location",
            "end_location",
            "ride_type",
            "vehicles",
            "title",
        ]
        read_only_fields = ["id"]
