import os
from twilio.rest import Client
from dotenv import load_dotenv

# Cargar variables
load_dotenv()

ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
FROM = os.getenv("TWILIO_WHATSAPP_FROM")
TO = os.getenv("MY_WHATSAPP")


def notify(message_text):
    if not ACCOUNT_SID or not AUTH_TOKEN:
        print("❌ Credenciales NO cargadas")
        return

    try:
        client = Client(ACCOUNT_SID, AUTH_TOKEN)

        message = client.messages.create(
            from_=FROM,
            body=message_text,
            to=TO
        )

        print("✅ MENSAJE ENVIADO:", message.sid)

    except Exception as e:
        print("❌ ERROR NOTIFIER:", str(e))