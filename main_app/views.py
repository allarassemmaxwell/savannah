"""
View functions for the MainApp Django application.
"""

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from .serializers import (
    CustomerSerializer,
    OrderSerializer
)


@api_view(['POST'])
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
def order_view(request):
    """
    Handle POST requests for Order.
    """
    if request.method == 'POST':
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)

        # Return validation errors if the data is invalid
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # This should never be reached in a properly configured API, as only POST is allowed
    return Response({"detail": "Method not allowed"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
