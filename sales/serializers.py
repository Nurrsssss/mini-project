from rest_framework import serializers
from .models import SalesOrder
from products.models import Product


class SalesOrderSerializer(serializers.ModelSerializer):
    product_id = serializers.PrimaryKeyRelatedField(
        queryset=Product.objects.all(), source='product', write_only=True
    )

    class Meta:
        model = SalesOrder
        fields = ['id', 'customer', 'product', 'product_id', 'quantity', 'total_price', 'created_at']
        read_only_fields = ['customer', 'total_price']

    def create(self, validated_data):
        request = self.context['request']
        validated_data['customer'] = request.user
        return super().create(validated_data)