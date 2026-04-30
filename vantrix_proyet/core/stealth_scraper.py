import requests
from bs4 import BeautifulSoup
from vantrix_proyet.core.logger import logger


def get_products(trend: str):
    logger.info(f"🔍 Buscando productos para: {trend}")

    try:
        url = f"https://www.amazon.com/s?k={trend.replace(' ', '+')}"
        headers = {
            "User-Agent": "Mozilla/5.0"
        }

        response = requests.get(url, headers=headers, timeout=5)

        if response.status_code != 200:
            raise Exception("Amazon bloqueó request")

        soup = BeautifulSoup(response.text, "html.parser")

        products = []

        for item in soup.select(".s-result-item")[:5]:
            title = item.select_one("h2")
            price = item.select_one(".a-price-whole")

            if title and price:
                products.append({
                    "title": title.text.strip(),
                    "selling_price": float(price.text.replace(",", "")),
                    "cost": float(price.text.replace(",", "")) * 0.6
                })

        if not products:
            raise Exception("No products parsed")

        logger.info("✅ Scraping real funcionando")
        return products

    except Exception as e:
        logger.warning(f"⚠️ Fallback activado: {e}")
        return _generate_mock_products(trend)


def _generate_mock_products(trend):
    logger.info("🧪 Generando productos simulados (modo seguro)")
    return [
        {"title": f"{trend} Pro X", "selling_price": 50, "cost": 20},
        {"title": f"{trend} Mini", "selling_price": 30, "cost": 10},
        {"title": f"{trend} Ultra", "selling_price": 80, "cost": 40},
        {"title": f"{trend} Lite", "selling_price": 25, "cost": 8},
        {"title": f"{trend} Max", "selling_price": 100, "cost": 60},
    ]