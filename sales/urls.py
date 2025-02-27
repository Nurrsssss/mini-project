from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SalesOrderViewSet, DiscountViewSet,download_invoice

router = DefaultRouter()
router.register(r"orders", SalesOrderViewSet)
router.register(r"discounts", DiscountViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("orders/<int:pk>/approve/", SalesOrderViewSet.as_view({"post": "approve_order"}), name="approve_order"),
    path("orders/<int:pk>/process/", SalesOrderViewSet.as_view({"post": "process_order"}), name="process_order"),
    path("orders/<int:pk>/invoice/", download_invoice, name="download_invoice"),
]
