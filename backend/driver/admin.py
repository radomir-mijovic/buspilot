from django.contrib import admin

from .models import Driver


@admin.register(Driver)
class DriverAdmin(admin.ModelAdmin):
    list_display = ["id", "company", "first_name", "last_name"]
    list_filter = ["company__name", "last_name", "first_name"]
