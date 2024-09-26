"""
View functions for the MainApp Django application.

This module contains the views that handle requests related to customers and orders.
It includes functionality for user registration and SMS notifications upon order creation.

- SignUpView: Allows users to register using the UserSerializer.
- customer_view: Handles POST requests for creating customers, returning validation errors as needed.
- order_view: Manages order creation, sends an SMS notification to the customer upon success,
    and handles errors appropriately.
"""


from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.exceptions import APIException
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import status, generics
from django.contrib.auth import get_user_model
from django.shortcuts import render

# Import your serializers and utility functions at the top
from .serializers import (
    CustomerSerializer,
    OrderSerializer,
    UserSerializer
)
from .utils import send_sms  # Import the SMS utility function

User = get_user_model()  # Get the user model


def home_view(request):
    """
    Handle index/home view.
    """
    context  = {}
    template = "index.html"
    return render(request, template, context)


class SignUpView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]  # Allow any user to register


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def customer_view(request):
    """
    Handle POST requests for Customer.
    """
    if request.method == 'POST':
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)

        # Return validation errors if the data is invalid
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # This should never be reached in a properly configured API, as only POST is allowed
    return Response({"detail": "Method not allowed"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def order_view(request):
    """
    Handle POST requests for Order.
    """
    if request.method == 'POST':
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            # Send SMS to the customer upon successful order creation
            order = serializer.save()
            message = f"Dear {order.customer.name}, your order for {order.item} has been successfully placed."
            try:
                send_sms('+254704205757', message)
            except APIException as e:
                return Response({"detail": str(e)}, status=status.HTTP_400_BAD_REQUEST)

            return Response(status=status.HTTP_201_CREATED)

        # Return validation errors if the data is invalid
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # This should never be reached in a properly configured API, as only POST is allowed
    return Response({"detail": "Method not allowed"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
