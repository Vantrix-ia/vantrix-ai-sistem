import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    APIFY_TOKEN = os.getenv("APIFY_TOKEN")
    SCRAPER_API_KEY = os.getenv("SCRAPER_API_KEY")
    RAINFOREST_API_KEY = os.getenv("RAINFOREST_API_KEY")

    TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
    TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
    TWILIO_WHATSAPP_FROM = os.getenv("TWILIO_WHATSAPP_FROM")
    MY_WHATSAPP = os.getenv("MY_WHATSAPP")

settings = Settings()