def analyze_product(product):
    selling_price = product.get("selling_price", 0)
    cost = product.get("cost", 0)

    profit = selling_price - cost
    margin = profit / selling_price if selling_price else 0

    product["profit"] = profit
    product["margin"] = margin

    return product