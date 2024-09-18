"""
Admin configuration for the main_app models.
"""

from django.contrib import admin
from .models import (
    Customer,
    Order
)


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    """
    Admin interface configuration for the Customer model.
    """
    date_hierarchy = 'timestamp'
    list_display = ['name', 'code', 'active', 'timestamp']
    list_display_links = ['name']
    list_filter = ['name', 'code']
    search_fields = ['name', 'code', 'active']
    list_per_page = 25

    class Meta:
        model = Customer

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    """
    Admin interface configuration for the Order model.
    """
    date_hierarchy = 'timestamp'
    list_display = ['item', 'amount', 'active', 'timestamp']
    list_display_links = ['item']
    list_filter = ['item', 'amount']
    search_fields = ['item', 'amount', 'active']
    list_per_page = 25

    class Meta:
        model = Order