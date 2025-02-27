from django.db import models
from sales.models import SalesOrder

class TradingAnalytics(models.Model):
    date = models.DateField(auto_now_add=True)
    total_trades = models.PositiveIntegerField(default=0)
    total_volume = models.DecimalField(max_digits=15, decimal_places=2, default=0.00)

    def __str__(self):
        return f"{self.date} - Trades: {self.total_trades}, Volume: {self.total_volume}"

class RevenueReport(models.Model):
    date = models.DateField(auto_now_add=True)
    total_revenue = models.DecimalField(max_digits=15, decimal_places=2, default=0.00)
    total_profit = models.DecimalField(max_digits=15, decimal_places=2, default=0.00)

    def __str__(self):
        return f"{self.date} - Revenue: {self.total_revenue}, Profit: {self.total_profit}"
