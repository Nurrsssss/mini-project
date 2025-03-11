from rest_framework import generics, permissions
from .models import SalesOrder
from .serializers import SalesOrderSerializer
from users.permissions import IsCustomer, IsAdmin

class SalesOrderListCreateView(generics.ListCreateAPIView):
    serializer_class = SalesOrderSerializer

    def get_queryset(self):
        user = self.request.user
        if user.is_admin():
            return SalesOrder.objects.all()  # Админ видит все заказы
        return SalesOrder.objects.filter(customer=user)  # Клиент видит только свои заказы

    def get_permissions(self):
        if self.request.method == 'POST':
            return [IsCustomer()]
        return [permissions.IsAuthenticated()]