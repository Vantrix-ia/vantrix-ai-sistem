from aliexpress_scraper import get_products

products = get_products("mini projector")

for p in products:
    print(p)