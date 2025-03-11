from django.contrib import admin
from .models import AnalyticsReport

@admin.register(AnalyticsReport)
class AnalyticsReportAdmin(admin.ModelAdmin):
    list_display = ("id", "report_type", "generated_by", "created_at")
    list_filter = ("report_type", "created_at")
    search_fields = ("generated_by__username",)