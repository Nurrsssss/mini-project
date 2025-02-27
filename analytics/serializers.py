from rest_framework import serializers
from .models import TradingAnalytics, RevenueReport

class TradingAnalyticsSerializer(serializers.ModelSerializer):
    class Meta:
        model = TradingAnalytics
        fields = ["date", "total_trades", "total_volume"]

class RevenueReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = RevenueReport
        fields = ["date", "total_revenue", "total_profit"]
