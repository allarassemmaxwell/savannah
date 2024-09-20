"""
Serializers for the main_app models.

This module defines serializers for User, Customer, and Order models,
    converting complex data types and handling validation.

- UserSerializer: Manages user creation with hashed passwords.
- CustomerSerializer: Handles Customer model data, with read-only fields.
- OrderSerializer: Manages Order model data, with specific fields read-only.
"""


from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import Customer, Order

User = get_user_model()  # Get the user model

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password', 'email']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User(**validated_data)
        user.set_password(validated_data['password'])  # Hash the password
        user.save()
        return user


class CustomerSerializer(serializers.ModelSerializer):
    """
    Serializer for the Customer model.
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
