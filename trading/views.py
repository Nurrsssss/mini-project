from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from .models import Order
from .serializers import OrderSerializer
from django.utils.timezone import now

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all().order_by("-created_at")
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.status != "pending":
            return Response({"error": "Only pending orders can be modified"}, status=status.HTTP_400_BAD_REQUEST)
        
        return super().update(request, *args, **kwargs)

    def execute_order(self, request, pk=None):
        order = self.get_object()
        if order.status != "pending":
            return Response({"error": "Only pending orders can be executed"}, status=status.HTTP_400_BAD_REQUEST)
        
        order.status = "executed"
        order.executed_at = now()
        order.save()
        return Response({"message": "Order executed successfully", "order": OrderSerializer(order).data})
