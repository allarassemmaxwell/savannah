"""
View functions for the MainApp Django application.
"""

from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

from .serializers import (
    CustomerSerializer,
    OrderSerializer
)
# from .utils import send_sms  # Import the SMS utility function


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
            serializer.save()
            # Send SMS to the customer upon successful order creation
            # order = serializer.save()
            # message = f"Dear {order.customer.name}, your order for {order.item} has been successfully placed."
            # send_sms('254704205757', message)

            return Response(status=status.HTTP_201_CREATED)

        # Return validation errors if the data is invalid
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # This should never be reached in a properly configured API, as only POST is allowed
    return Response({"detail": "Method not allowed"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
