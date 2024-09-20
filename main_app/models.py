"""
Models for the main_app application.

This module defines the Customer and Order models, which store information about customers and their orders.

- Customer: Represents a customer with attributes like name, unique code, and status.
- Order: Represents an order with details such as the associated customer, item, amount, and status.
"""


from django.db import models

class Customer(models.Model):
    """
    Model for Customer.
    Stores basic customer information such as name, code, and status.
    """
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=100, unique=True)
    active = models.BooleanField(("Active"), default=True)
    timestamp = models.DateTimeField(
        ("Created At"), auto_now_add=True
    )
    updated = models.DateTimeField(
        ("Updated At"), auto_now=True
    )

    def __str__(self):
        return self.name


class Order(models.Model):
    """
    Model for Order.
    Stores order details such as customer, item, amount, and status.
    Automatically generates a slug for the order.
    """
    customer = models.ForeignKey(Customer, related_name='orders', on_delete=models.CASCADE)
    item = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    active = models.BooleanField(("Active"), default=True)
    timestamp = models.DateTimeField(
        ("Created At"), auto_now_add=True
    )
    updated = models.DateTimeField(
        ("Updated At"), auto_now=True
    )
    slug = models.SlugField(
        ("Slug"), max_length=255, null=True, blank=True, editable=False
    )

    def __str__(self):
        return f"Order {self.item} by {self.customer.name}"
