from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from django.utils.timezone import now
from .models import SalesOrder, Discount
from .serializers import SalesOrderSerializer, DiscountSerializer
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from .utils import generate_invoice_pdf
from django.core.mail import send_mail


def download_invoice(request, pk):
    order = get_object_or_404(SalesOrder, pk=pk)
    return generate_invoice_pdf(order) or HttpResponse("Error generating invoice", status=500)

class DiscountViewSet(viewsets.ModelViewSet):
    queryset = Discount.objects.all()
    serializer_class = DiscountSerializer
    permission_classes = [permissions.IsAuthenticated]

class SalesOrderViewSet(viewsets.ModelViewSet):
    queryset = SalesOrder.objects.all().order_by("-created_at")
    serializer_class = SalesOrderSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(customer=self.request.user)

    def approve_order(self, request, pk=None):
        order = self.get_object()
        if order.status != "pending":
            return Response({"error": "Only pending orders can be approved"}, status=status.HTTP_400_BAD_REQUEST)
        
        order.status = "approved"
        order.save()
        return Response({"message": "Order approved successfully", "order": SalesOrderSerializer(order).data})

    def process_order(self, request, pk=None):
        order = self.get_object()
        if order.status != "approved":
            return Response({"error": "Only approved orders can be processed"}, status=status.HTTP_400_BAD_REQUEST)
        
        order.status = "processed"
        order.processed_at = now()
        order.save()
        return Response({"message": "Order processed successfully", "order": SalesOrderSerializer(order).data})
    
def send_trade_notification(user_email, trade_details):
    send_mail(
        "Trade Execution Notification",
        f"Your trade has been executed: {trade_details}",
        "your-email@gmail.com",
        [user_email],
        fail_silently=False,
    )
