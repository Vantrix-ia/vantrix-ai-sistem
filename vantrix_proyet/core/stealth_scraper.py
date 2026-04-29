import requests
import os
from dotenv import load_dotenv

# 🔌 externos
from vantrix_proyet.core.shopify_scraper import get_shopify_products
from vantrix_proyet.core.tiktok_scraper import get_tiktok_products

# 🔐 cargar .env
load_dotenv()

API_KEY = os.getenv("RAINFOREST_API_KEY")


# ================================
# 🛒 AMAZON SCRAPER
# ================================
def get_amazon_products(trend):
    print(f"🛒 Buscando en Amazon: {trend}")

    if not API_KEY:
        print("❌ No API KEY de Rainforest")
        return []

    url = "https://api.rainforestapi.com/request"

    params = {
        "api_key": API_KEY,
        "type": "search",
        "amazon_domain": "amazon.com",
        "search_term": trend
    }

    try:
        response = requests.get(url, params=params)
        data = response.json()
    except Exception as e:
        print(f"❌ ERROR Amazon: {e}")
        return []

    products = []

    for item in data.get("search_results", [])[:5]:
        try:
            price = item.get("price", {}).get("value", 20)

            products.append({
                "title": item.get("title"),
                "cost": round(price * 0.5, 2),
                "selling_price": price,
                "rating": 4.5,
                "reviews": 1000,
                "trend_score": 8
            })

        except:
            continue

    print(f"✅ Amazon productos: {len(products)}")
    return products


# ================================
# 🧠 MASTER FUNCTION (CLAVE)
# ================================
def get_products(trend):
    print("\n🚀 MULTI-SOURCE SCRAPER ACTIVADO\n")

    amazon_products = get_amazon_products(trend)
    shopify_products = get_shopify_products()
    tiktok_products = get_tiktok_products()

    all_products = amazon_products + shopify_products + tiktok_products

    print(f"🔥 TOTAL productos: {len(all_products)}")

    return all_products