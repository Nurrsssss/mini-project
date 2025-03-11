from django.urls import path
from .views import GenerateSalesReportView, GenerateTradingReportView, GenerateProfitLossReportView

urlpatterns = [
    path('sales-report/', GenerateSalesReportView.as_view(), name='generate-sales-report'),
    path('trading-report/', GenerateTradingReportView.as_view(), name='generate-trading-report'),
    path('profit-loss-report/', GenerateProfitLossReportView.as_view(), name='generate-profit-loss-report'),
]