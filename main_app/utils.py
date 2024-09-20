# import africastalking
# from django.conf import settings

# # Initialize Africa's Talking SDK
# africastalking.initialize(
#     settings.AFRICAS_TALKING_USERNAME,
#     settings.AFRICAS_TALKING_API_KEY
# )

# sms = africastalking.SMS

# def send_sms(phone_number, message):
#     try:
#         response = sms.send(message, [phone_number])
#         print(response)
#     except Exception as e:
#         print(f"Error sending SMS: {e}")
