def enrich_product(product):
    product["profit"] = product["selling_price"] - product["cost"]
    product["margin"] = product["profit"] / product["selling_price"]
    return product