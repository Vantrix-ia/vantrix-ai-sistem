import random

def get_products():
    products = []

    for i in range(20):
        products.append({
            "id": i,
            "title": f"Producto {i}",
            "price": round(random.uniform(5, 100), 2),
            "rating": round(random.uniform(3.5, 5.0), 2),
            "reviews": random.randint(10, 500),
        })

    return products