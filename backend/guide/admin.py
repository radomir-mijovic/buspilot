from django.contrib import admin

from .models import Guide

@admin.register(Guide)
class GuideAdmin(admin.ModelAdmin):
    list_display = ["id", "last_name", "company"]
