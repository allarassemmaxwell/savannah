"""
Utility functions for the MainApp Django application.

This module contains helper functions for sending SMS notifications using the Africa's Talking SDK.

- send_sms: Sends an SMS to the specified phone number with the provided message.
    Handles specific and general exceptions, allowing the calling view to manage errors.
"""


import africastalking
from django.conf import settings

# Initialize Africa's Talking SDK
africastalking.initialize(
    settings.AFRICAS_TALKING_USERNAME,
    settings.AFRICAS_TALKING_API_KEY
)

SMS = africastalking.SMS

def send_sms(phone_number, message):
    try:
        response = SMS.send(message, [phone_number])
        print(response)
    except ValueError as e:
        print(f"Value error: {e}")  # Specific handling for value errors
        raise  # Reraise the exception to handle it in the view
    except Exception as e:
        print(f"Error sending SMS: {e}")  # General exception handling
        raise  # Reraise the exception to handle it in the view
