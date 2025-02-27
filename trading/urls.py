from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import OrderViewSet

router = DefaultRouter()
router.register(r"orders", OrderViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("orders/<int:pk>/execute/", OrderViewSet.as_view({"post": "execute_order"}), name="execute_order"),
]
