from django.db import models
from django.contrib.auth import get_user_model
from products.models import Product

User = get_user_model()

class Order(models.Model):
    ORDER_TYPES = [
        ("buy", "Buy"),
        ("sell", "Sell"),
    ]
    STATUS_CHOICES = [
        ("pending", "Pending"),
        ("executed", "Executed"),
        ("canceled", "Canceled"),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="orders")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="orders")
    order_type = models.CharField(max_length=10, choices=ORDER_TYPES)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="pending")
    created_at = models.DateTimeField(auto_now_add=True)
    executed_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.user} {self.order_type} {self.quantity} {self.product} at {self.price}"
