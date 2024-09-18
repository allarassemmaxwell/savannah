from rest_framework import serializers
from .models import Customer, Order


class CustomerSerializer(serializers.ModelSerializer):
    """
    Serializer for the Customer model.

    This class handles the conversion of Order objects to and from
    JSON, as well as the validation of input data.
    """

    class Meta:
        model = Customer
        fields = [
            'id',
            'name',
            'code',
            'active',
            'timestamp'
        ]
        read_only_fields = ['id', 'timestamp']  # These fields cannot be modified directly



class OrderSerializer(serializers.ModelSerializer):
    """
    Serializer for the Order model.

    This class handles the conversion of Order objects to and from
    JSON, as well as the validation of input data.
    """

    class Meta:
        model = Order
        fields = [
            'id',
            'customer',
            'item',
            'amount',
            'active',
            'timestamp',
            'slug'
        ]
        read_only_fields = ['id', 'timestamp', 'slug']  # These fields cannot be modified directly


