from django.db import models
from django.db import transaction
from products.models import Product
from users.models import User

class SalesOrder(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE, related_name="sales_orders")  # Изменили related_name
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="sales_orders")  # Изменили related_name
    quantity = models.PositiveIntegerField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if self.pk is None:
            with transaction.atomic():
                self.product.reduce_stock(self.quantity)
                self.total_price = self.product.price * self.quantity
                super().save(*args, **kwargs)
        else:
            super().save(*args, **kwargs)

    def __str__(self):
        return f"Order {self.id} - {self.customer.username} - {self.product.name}"