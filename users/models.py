from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    class Role(models.TextChoices):
        ADMIN = "admin", "Admin"
        TRADER = "trader", "Trader"
        SALES = "sales", "Sales Representative"
        CUSTOMER = "customer", "Customer"

    role = models.CharField(max_length=20, choices=Role.choices, default=Role.CUSTOMER)
    profile_image = models.ImageField(upload_to='profile_images/', blank=True, null=True)

    def is_admin(self):
        return self.role == self.Role.ADMIN

    def is_trader(self):
        return self.role == self.Role.TRADER

    def is_sales(self):
        return self.role == self.Role.SALES

    def is_customer(self):
        return self.role == self.Role.CUSTOMER