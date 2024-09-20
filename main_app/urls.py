"""
URL configurations for the MainApp Django application.
"""

from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .views import (
    customer_view,
    order_view
)

urlpatterns = [
    path('customers/', customer_view, name='customer_view'),
    path('orders/', order_view, name='order_view'),
    # JWT token paths
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
