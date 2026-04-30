import requests

def get_shopify_products():
    print("🛍️ Buscando en Shopify...")

    # puedes cambiar esta tienda por cualquier Shopify pública
    url = "https://gymshark.com/products.json"

    try:
        res = requests.get(url)
        data = res.json()
    except Exception as e:
        print(f"❌ ERROR Shopify: {e}")
        return []

    products = []

    for p in data.get("products", [])[:5]:
        try:
            price = float(p["variants"][0]["price"])

            products.append({
                "title": p["title"],
                "cost": round(price * 0.5, 2),
                "selling_price": price,
                "rating": 4.5,
                "reviews": 300,
                "trend_score": 7
            })

        except:
            continue

    print(f"✅ Shopify productos: {len(products)}")
    return products