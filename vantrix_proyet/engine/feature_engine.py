from vantrix_proyet.core.models import Product


def analyze_product(product_dict):

    product = Product(
        title=product_dict.get("title"),
        cost=product_dict.get("cost", 0),
        selling_price=product_dict.get("selling_price", 0)
    )

    product.profit = product.selling_price - product.cost

    if product.selling_price > 0:
        product.margin = product.profit / product.selling_price
    else:
        product.margin = 0

    return product