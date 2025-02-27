from django.db import models
from django.contrib.auth import get_user_model
from products.models import Product

User = get_user_model()

class Discount(models.Model):
    name = models.CharField(max_length=255)
    percentage = models.DecimalField(max_digits=5, decimal_places=2, help_text="Percentage discount (e.g. 10 for 10%)")
    active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name} - {self.percentage}%"

class SalesOrder(models.Model):
    STATUS_CHOICES = [
        ("pending", "Pending"),
        ("approved", "Approved"),
        ("processed", "Processed"),
        ("canceled", "Canceled"),
    ]

    customer = models.ForeignKey(User, on_delete=models.CASCADE, related_name="sales_orders")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="sales_orders")
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount = models.ForeignKey(Discount, on_delete=models.SET_NULL, null=True, blank=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="pending")
    created_at = models.DateTimeField(auto_now_add=True)
    processed_at = models.DateTimeField(null=True, blank=True)

    def save(self, *args, **kwargs):
        if self.discount:
            self.total_price = self.price * self.quantity * (1 - (self.discount.percentage / 100))
        else:
            self.total_price = self.price * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Order {self.id} - {self.customer} ({self.status})"
