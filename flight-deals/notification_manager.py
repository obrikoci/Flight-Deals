from twilio.rest import Client

TWILIO_SID = "AC1f8ae4df7a706685d9211e91744eb6d9"
TWILIO_AUTH_TOKEN = "729096d8613b7f0803143d2da0ebaf84"
TWILIO_VIRTUAL_NUMBER = "+12512374542"
TWILIO_VERIFIED_NUMBER = "+355692074793"


class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )
        # Prints if successfully sent
        print(message.sid)
