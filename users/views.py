from rest_framework import generics, permissions
from django.contrib.auth import get_user_model
from rest_framework.response import Response

from .serializers import UserSerializer
from .permissions import IsAdmin, IsTrader, IsSalesRepresentative

User = get_user_model()

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        return Response({"message": "User registered successfully!", "user": response.data})

class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdmin]

class TraderDashboardView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsTrader]

class SalesDashboardView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsSalesRepresentative]