from rest_framework import serializers
from .models import SalesOrder, Discount

class DiscountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Discount
        fields = ["id", "name", "percentage", "active"]

class SalesOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = SalesOrder
        fields = ["id", "customer", "product", "quantity", "price", "discount", "total_price", "status", "created_at", "processed_at"]
        read_only_fields = ["customer", "total_price", "status", "created_at", "processed_at"]
