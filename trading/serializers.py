from rest_framework import serializers
from .models import Order

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ["id", "user", "product", "order_type", "quantity", "price", "status", "created_at", "executed_at"]
        read_only_fields = ["user", "status", "created_at", "executed_at"]
