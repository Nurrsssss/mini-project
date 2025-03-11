from django.urls import path
from .views import ProductViewSet, CategoryViewSet

urlpatterns = [
    path('categories/', CategoryViewSet.as_view({'get': 'list', 'post': 'create'}), name='category-list'),
    path('categories/<int:pk>/', CategoryViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='category-detail'),

    path('', ProductViewSet.as_view({'get': 'list', 'post': 'create'}), name='product-list'),
    path('<int:pk>/', ProductViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='product-detail'),
]