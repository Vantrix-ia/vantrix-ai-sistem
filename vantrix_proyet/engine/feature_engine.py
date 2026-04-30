def analyze_product(raw_product: dict):

    # 🔥 Simple: ya viene limpio del scraper
    return {
        "title": raw_product["title"],
        "selling_price": raw_product["selling_price"],
        "cost": raw_product["cost"],
        "rating": raw_product.get("rating", 4.0),
        "reviews": raw_product.get("reviews", 100),
    }