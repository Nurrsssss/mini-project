from django.db.models import Sum, Count
from rest_framework import generics, permissions
from sales.models import SalesOrder
from .models import TradingAnalytics, RevenueReport
from .serializers import TradingAnalyticsSerializer, RevenueReportSerializer
from django.http import HttpResponse
import csv
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from .utils import generate_report_pdf

def download_report_pdf(request):
    report_data = RevenueReport.objects.all().order_by("-date")
    return generate_report_pdf(report_data) or HttpResponse("Error generating report", status=500)

class TradingAnalyticsView(generics.ListAPIView):
    queryset = TradingAnalytics.objects.all()
    serializer_class = TradingAnalyticsSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Calculate total trades and volume
        return TradingAnalytics.objects.all().order_by("-date")

class RevenueReportView(generics.ListAPIView):
    queryset = RevenueReport.objects.all()
    serializer_class = RevenueReportSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Generate revenue reports dynamically
        return RevenueReport.objects.all().order_by("-date")

def export_sales_csv(request):
    """Generate CSV report for sales data"""
    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = 'attachment; filename="sales_report.csv"'

    writer = csv.writer(response)
    writer.writerow(["Date", "Customer", "Product", "Quantity", "Total Price", "Status"])

    sales_orders = SalesOrder.objects.all()
    for order in sales_orders:
        writer.writerow([order.created_at, order.customer.username, order.product.name, order.quantity, order.total_price, order.status])

    return response
