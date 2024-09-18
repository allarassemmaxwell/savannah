"""
URL configurations for the MainApp Django application.
"""

from django.urls import path
from .views import (
    customer_view,
    order_view
)

urlpatterns = [
    path('customers/', customer_view, name='customer_view'),
    path('orders/', order_view, name='order_view'),
]
