from django.contrib import admin

from .models import Ride


@admin.register(Ride)
class RideAdmin(admin.ModelAdmin):
    list_display = ["title", "company", "ride_type"]
    list_filter = ["title", "company__name"]

    fields = [
        "title",
        "description",
        "is_all_day",
        "ride_type",
        "company",
        "vehicles",
        "drivers",
        "start_time",
        "end_time",
        "start_date",
        "end_date",
        "start_location",
        "end_location",
    ]
