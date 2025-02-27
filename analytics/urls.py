from django.urls import path
from .views import TradingAnalyticsView, RevenueReportView, export_sales_csv, download_report_pdf

urlpatterns = [
    path("trading/", TradingAnalyticsView.as_view(), name="trading_analytics"),
    path("revenue/", RevenueReportView.as_view(), name="revenue_report"),
    path("export/csv/", export_sales_csv, name="export_sales_csv"),
    path("export/pdf/", download_report_pdf, name="export_report_pdf"),
]
