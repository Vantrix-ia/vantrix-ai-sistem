from playwright.sync_api import sync_playwright
import time
import random


def get_products(query="mini projector"):
    products = []

    with sync_playwright() as p:
        browser = p.chromium.launch(
            headless=False,
            args=["--disable-blink-features=AutomationControlled"]
        )

        context = browser.new_context(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/120 Safari/537.36",
            viewport={"width": 1280, "height": 800}
        )

        page = context.new_page()

        url = f"https://www.aliexpress.com/wholesale?SearchText={query}"
        page.goto(url)

        # Espera tipo humano
        time.sleep(random.uniform(4, 7))

        # Scroll humano
        for _ in range(5):
            page.mouse.wheel(0, random.randint(1000, 3000))
            time.sleep(random.uniform(1, 3))

        # Detectar bloqueo
        if "Sorry" in page.content():
            print("🚫 AliExpress te bloqueó (captcha)")
            browser.close()
            return []

        items = page.query_selector_all("div[data-product-id]")

        print(f"Productos encontrados: {len(items)}")

        for item in items[:10]:
            try:
                name = item.query_selector("h3").inner_text()
                price = item.query_selector(".price").inner_text()

                products.append({
                    "name": name,
                    "price": price,
                    "rating": 4.5,
                    "reviews": 1000,
                    "profit": 30,
                    "margin": 40,
                    "v_score": 9.0,
                    "decision": "WINNER",
                    "trend_source": "aliexpress"
                })

            except:
                continue

        browser.close()

    return products