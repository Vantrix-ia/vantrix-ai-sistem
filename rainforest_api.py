import requests
import time
import random

# 🔑 PON AQUÍ TU API KEY
API_KEY = "4C0B11B902C44D46B38BCADE40671521"


class RainforestAPI:

    @staticmethod
    def search_products(query, limit=5):
        url = "https://api.rainforestapi.com/request"

        params = {
            "api_key": API_KEY,
            "type": "search",  # 🔥 MUY IMPORTANTE
            "amazon_domain": "amazon.com",
            "search_term": query
        }

        try:
            print(f"🔎 Buscando: {query}")

            response = requests.get(url, params=params, timeout=15)

            if response.status_code != 200:
                print(f"❌ HTTP Error: {response.status_code}")
                return []

            data = response.json()

            results = data.get("search_results", [])

            if not results:
                print("⚠️ No hay resultados en API")
                return []

            products = []

            for item in results[:limit]:
                product = {
                    "name": item.get("title"),
                    "price": RainforestAPI.extract_price(item),
                    "rating": item.get("rating", 0),
                    "reviews": item.get("ratings_total", 0),
                    "link": item.get("link"),
                }

                products.append(product)

            print(f"✅ {len(products)} productos encontrados para '{query}'")

            # 🔥 delay humano para evitar rate limit
            time.sleep(random.uniform(1, 2))

            return products

        except Exception as e:
            print(f"❌ API ERROR: {e}")
            return []

    @staticmethod
    def extract_price(item):
        """
        Maneja TODOS los formatos posibles de precio
        """
        price = item.get("price")

        # Caso 1: dict (el correcto)
        if isinstance(price, dict):
            return price.get("value", 0)

        # Caso 2: string tipo "$12.99"
        if isinstance(price, str):
            try:
                return float(price.replace("$", "").replace(",", ""))
            except:
                return 0

        return 0