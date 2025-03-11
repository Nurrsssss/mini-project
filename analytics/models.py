from django.db import models
from users.models import User

class AnalyticsReport(models.Model):
    REPORT_TYPES = [
        ('sales', 'Sales Report'),
        ('trading', 'Trading Report'),
        ('profit_loss', 'Profit/Loss Report')
    ]

    report_type = models.CharField(max_length=20, choices=REPORT_TYPES)
    generated_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    data = models.JSONField()

    def __str__(self):
        return f"{self.get_report_type_display()} ({self.created_at})"