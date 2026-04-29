def calculate_financials(features):
    price = features.get("price", 0)

    cost = price * 0.4
    shipping = features.get("shipping_cost", 3)

    profit = price - cost - shipping

    if price == 0:
        margin = 0
    else:
        margin = profit / price

    return {
        "profit": round(profit, 2),
        "margin": round(margin, 2)
    }