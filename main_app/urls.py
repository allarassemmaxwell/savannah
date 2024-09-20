"""
URL configurations for the MainApp Django application.

This module defines the URL patterns for the API endpoints,
    facilitating the routing of requests to the appropriate views.

- customer_view: Endpoint for managing customer data.
- order_view: Endpoint for handling order transactions.
- JWT token paths: Endpoints for obtaining and refreshing JWT tokens for authentication.
- SignUpView: Endpoint for user registration.
"""


from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .views import (
    customer_view,
    order_view,
    SignUpView,
)

urlpatterns = [
    path('customers/', customer_view, name='customer_view'),
    path('orders/', order_view, name='order_view'),
    # JWT token paths
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # Sign up path
    path('signup/', SignUpView.as_view(), name='signup'),
]
