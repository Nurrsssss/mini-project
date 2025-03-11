from django.urls import path
from .views import SalesOrderListCreateView

urlpatterns = [
    path('orders/', SalesOrderListCreateView.as_view(), name='sales-orders'),
]
