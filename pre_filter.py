def filter_products(products):
    filtered = []

    for p in products:
        price = p.get("price", 0)
        rating = p.get("rating", 0)
        reviews = p.get("reviews", 0)
        is_saturated = p.get("is_saturated", True)

        # 🔥 FILTRO PRO
        if price < 10:
            continue

        if rating < 3.8:
            continue

        if reviews < 50:
            continue

        if is_saturated:
            continue

        filtered.append(p)

    print(f"🧠 Filtro PRO: {len(filtered)} / {len(products)} pasan")
    return filtered