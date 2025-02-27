from django.urls import path
from .views import notification_list  # Make sure this function exists!

urlpatterns = [
    path('', notification_list, name='notification_list'),
]
