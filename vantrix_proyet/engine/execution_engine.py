from shopify_client import create_product
from database import save_winner

def publish(product):
    # evitar duplicados
    if not save_winner(product):
        print("⚠️ YA EXISTE - SKIP")
        return

    try:
        create_product(
            title=product["title"],
            price=product["selling_price"]
        )
        print("✅ PUBLICADO EN SHOPIFY")

    except Exception as e:
        print("❌ ERROR PUBLICANDO:", e)