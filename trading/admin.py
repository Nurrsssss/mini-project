from django.contrib import admin
from .models import Order, Transaction

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "product", "order_type", "quantity", "price_per_unit", "created_at")
    list_filter = ("order_type", "product", "created_at")
    search_fields = ("user__username", "product__name")

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ("id", "buyer", "seller", "product", "quantity", "total_price", "created_at")
    list_filter = ("product", "created_at")
    search_fields = ("buyer__username", "seller__username", "product__name")