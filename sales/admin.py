from django.contrib import admin
from .models import SalesOrder

@admin.register(SalesOrder)
class SalesOrderAdmin(admin.ModelAdmin):
    list_display = ("id", "customer", "product", "quantity", "total_price", "created_at")
    list_filter = ("product", "created_at")
    search_fields = ("customer__username", "product__name")