from django.contrib import admin

from .models import Defect

@admin.register(Defect)
class DefectAdmin(admin.ModelAdmin):
    list_display = ["id", "company"]

