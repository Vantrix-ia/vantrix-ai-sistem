import requests
import os
from dotenv import load_dotenv

# =========================
# CONFIG
# =========================
load_dotenv()

API_KEY = os.getenv("RAINFOREST_API_KEY")


# =========================
# MAIN SCRAPER FUNCTION
# =========================
def get_products(trend):
    print(f"🔎 Buscando en Amazon: {trend}")

    if not API_KEY:
        print("❌ ERROR: No se encontró API KEY")
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
        print(f"❌ ERROR llamando API: {e}")
        return []

    products = []

    results = data.get("search_results", [])

    if not results:
        print("⚠️ No se encontraron resultados en Amazon")
        return []

    for item in results[:5]:
        try:
            price = item.get("price", {}).get("value", 20)

            product = {
                "title": item.get("title", "N/A"),
                "cost": round(price * 0.5, 2),  # estimación
                "selling_price": price,
                "rating": item.get("rating", 4),
                "reviews": item.get("ratings_total", 100),
                "trend_score": 8
            }

            products.append(product)

        except Exception as e:
            print(f"⚠️ Error procesando producto: {e}")

    print(f"✅ Productos reales obtenidos: {len(products)}")
    return products