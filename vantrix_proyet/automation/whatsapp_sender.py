from twilio.rest import Client
import os
from dotenv import load_dotenv

load_dotenv()

ACCOUNT_SID = os.getenv("TWILIO_SID")
AUTH_TOKEN = os.getenv("TWILIO_TOKEN")
FROM = os.getenv("TWILIO_WHATSAPP_FROM")
TO = os.getenv("MY_WHATSAPP")

client = Client(ACCOUNT_SID, AUTH_TOKEN)


def send_whatsapp_message(message):
    try:
        client.messages.create(
            body=message,
            from_=f"whatsapp:{FROM}",
            to=f"whatsapp:{TO}"
        )
        print("✅ Mensaje enviado a WhatsApp")
    except Exception as e:
        print("❌ Error WhatsApp:", e)