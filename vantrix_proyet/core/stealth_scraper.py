from apify_client import ApifyClient
from vantrix_proyet.config.settings import settings


def get_products(trend):
    client = ApifyClient(settings.APIFY_TOKEN)

    run_input = {
        "search": trend,
        "maxItems": 5
    }

    run = client.actor("apify/amazon-product-scraper").call(run_input=run_input)

    products = []

    for item in client.dataset(run["defaultDatasetId"]).iterate_items():
        products.append({
            "title": item.get("title"),
            "selling_price": item.get("price", 0),
            "cost": item.get("price", 0) * 0.5  # estimación inicial
        })

    return products