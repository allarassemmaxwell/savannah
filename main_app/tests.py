"""
Tests for the MainApp Django application.

This module contains tests for the views that handle requests related to customers and orders.

- SignUpView: Tests for user registration functionality.
- CustomerAPITest: Tests for creating and managing customers.
- OrderAPITest: Tests for creating and managing orders.
"""

# Standard library imports
from django.urls import reverse
from django.contrib.auth import get_user_model

# Third-party imports
from rest_framework import status
from rest_framework.test import APITestCase, APIClient

# Local application imports
from .models import Customer, Order

User = get_user_model()

class SignUpAPITest(APITestCase):

    def setUp(self):
        self.signup_url = reverse('signup')

    def test_signup_user(self):
        """
        Test user signup with valid data.
        """
        response = self.client.post(self.signup_url, {
            'username': 'testuser',
            'password': 'testpassword',
            'email': 'test@example.com'
        })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(User.objects.get().username, 'testuser')


class CustomerAPITest(APITestCase):

    def setUp(self):
        self.client = APIClient()
        self.signup_url = reverse('signup')
        self.customer_url = reverse('customer_view')

        # Create a user for authentication
        self.client.post(self.signup_url, {
            'username': 'testuser',
            'password': 'testpassword',
            'email': 'test@example.com'
        })

        # Obtain JWT token
        response = self.client.post(reverse('token_obtain_pair'), {
            'username': 'testuser',
            'password': 'testpassword'
        })
        self.token = response.data['access']
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token)  # Set the token for authentication

        self.customer_data = {
            'name': 'Test Customer',
            'code': 'CUST123',
            'active': True
        }

    def test_create_customer(self):
        """
        Ensure we can create a new Customer object via the API.
        """
        response = self.client.post(self.customer_url, self.customer_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Customer.objects.count(), 1)
        self.assertEqual(Customer.objects.get().name, 'Test Customer')

    def test_create_customer_invalid_data(self):
        """
        Ensure that invalid data results in a bad request response.
        """
        invalid_data = {
            'name': '',
            'code': 'CUST123',  # Unique constraint violation if same code is used
            'active': True
        }

        response = self.client.post(self.customer_url, invalid_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Customer.objects.count(), 0)  # No new customer should be created

    def test_create_customer_unauthenticated(self):
        """
        Test creating a customer when not authenticated.
        """
        self.client.force_authenticate(user=None)  # Force unauthenticated state
        response = self.client.post(self.customer_url, self.customer_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


class OrderAPITest(APITestCase):

    def setUp(self):
        self.client = APIClient()
        self.signup_url = reverse('signup')
        self.order_url = reverse('order_view')

        # Create a user for authentication
        self.client.post(self.signup_url, {
            'username': 'testuser',
            'password': 'testpassword',
            'email': 'test@example.com'
        })

        # Obtain JWT token
        response = self.client.post(reverse('token_obtain_pair'), {
            'username': 'testuser',
            'password': 'testpassword'
        })
        self.token = response.data['access']
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token)  # Set the token for authentication

        self.customer = Customer.objects.create(
            name='Test Customer',
            code='CUST123',
            active=True
        )
        self.order_data = {
            'customer': self.customer.id,
            'item': 'Test Item',
            'amount': 100.00,
            'active': True
        }

    def test_create_order(self):
        """
        Ensure we can create a new Order object via the API.
        """
        response = self.client.post(self.order_url, self.order_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Order.objects.count(), 1)
        self.assertEqual(Order.objects.get().item, 'Test Item')

    def test_create_order_invalid_data(self):
        """
        Ensure that invalid data results in a bad request response.
        """
        invalid_order_data = {
            'customer': '',  # Invalid customer ID
            'item': '',      # Invalid item
            'amount': -50.00,  # Invalid amount (negative)
            'active': True
        }

        response = self.client.post(self.order_url, invalid_order_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Order.objects.count(), 0)  # No new order should be created

    def test_create_order_unauthenticated(self):
        """
        Test creating an order when not authenticated.
        """
        self.client.force_authenticate(user=None)  # Force unauthenticated state
        response = self.client.post(self.order_url, self.order_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
