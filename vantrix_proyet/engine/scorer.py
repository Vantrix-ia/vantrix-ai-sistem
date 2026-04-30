import random

def calculate_scores(product):
    product["trend_score"] = random.uniform(0.6, 0.9)
    product["saturation_score"] = random.uniform(0.2, 0.6)
    product["branding_score"] = random.uniform(0.4, 0.8)

    return product