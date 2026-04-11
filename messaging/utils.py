import requests
from messaging.models import SmsLog
from messaging.api.hamwesms import MessagingOperations as operator


def send_sms(recipient: str, message: str, sender: str = None):
    try:
        payload = {
            "to": recipient,
            "message": message,
            "sender": sender
        }
        # Example: POST to your SMS gateway
        # response = requests.post("https://sms-api.example.com/send", json=payload)
        # response_data = response.json()
        response = operator.send_message(recipient, message)
        status = "SUCCESS" if response == "SUCCESS" else "FAILED"

        # Log SMS attempt
        SmsLog.objects.create(
            recipient=recipient,
            message=message,
            status=status,
            api_response=response_data,
            sender=sender
        )

        return response_data

    except Exception as e:
        # Log exception
        SmsLog.objects.create(
            recipient=recipient,
            message=message,
            status="ERROR",
            error=str(e),
            sender=sender
        )
        raise e