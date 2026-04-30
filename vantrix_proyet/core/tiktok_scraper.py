from apify_client import ApifyClient
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("APIFY_API_KEY")

def get_tiktok_products():
    print("📱 Buscando en TikTok...")

    if not API_KEY:
        print("❌ No API KEY TikTok")
        return []

    client = ApifyClient(API_KEY)

    try:
        run = client.actor("clockworks/tiktok-scraper").call(
            run_input={"search": "viral products"}
        )

        items = client.dataset(run["defaultDatasetId"]).list_items().items

    except Exception as e:
        print(f"❌ ERROR TikTok: {e}")
        return []

    products = []

    for item in items[:5]:
        products.append({
            "title": item.get("desc", "TikTok Product"),
            "cost": 10,
            "selling_price": 25,
            "rating": 4.5,
            "reviews": 1000,
            "trend_score": 9
        })

    print(f"✅ TikTok productos: {len(products)}")
    return products