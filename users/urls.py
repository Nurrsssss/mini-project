from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import RegisterView,UserListView, TraderDashboardView, SalesDashboardView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', TokenObtainPairView.as_view(), name='login'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('users/', UserListView.as_view(), name='users'),
    path('trader-dashboard/', TraderDashboardView.as_view(), name='trader_dashboard'),
    path('sales-dashboard/', SalesDashboardView.as_view(), name='sales_dashboard'),
]