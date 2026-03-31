from django.contrib import admin

from .models import Vehicle, VehicleDocument


@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    list_display = ["id", "brand"]


@admin.register(VehicleDocument)
class VehicleDocumentAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "vehicle"]
