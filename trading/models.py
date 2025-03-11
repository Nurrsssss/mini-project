from django.db import models
from users.models import User
from products.models import Product

class Order(models.Model):
    ORDER_TYPE_CHOICES = [
        ('buy', 'Buy'),
        ('sell', 'Sell'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="trade_orders")  # Изменяем related_name
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="trade_orders")  # Изменяем related_name
    order_type = models.CharField(max_length=4, choices=ORDER_TYPE_CHOICES)
    quantity = models.PositiveIntegerField()
    price_per_unit = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if self.order_type == "sell" and self.pk is None:
            if self.product.stock < self.quantity:
                raise ValueError(f"Недостаточно товара {self.product.name} на складе!")
        super().save(*args, **kwargs)


class Transaction(models.Model):
    buyer = models.ForeignKey(User, on_delete=models.CASCADE, related_name="bought_transactions")
    seller = models.ForeignKey(User, on_delete=models.CASCADE, related_name="sold_transactions")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="transactions")
    quantity = models.PositiveIntegerField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Transaction: {self.buyer.username} bought {self.quantity}x {self.product.name} from {self.seller.username}"