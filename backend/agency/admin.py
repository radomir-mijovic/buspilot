from django.contrib import admin

from .models import Agency, AgencyDocument


@admin.register(Agency)
class AgencyAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "company"]
    list_filter = ["company__name", "name"]

@admin.register(AgencyDocument)
class AgencyDocumentAdmin(admin.ModelAdmin):
    list_display = ["id", "agency", "title"]
