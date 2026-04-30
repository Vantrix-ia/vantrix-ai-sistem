def evaluate_product(product):
    score = 0

    # Rating
    if product["rating"] >= 4.5:
        score += 3
    elif product["rating"] >= 4.2:
        score += 2

    # Reviews
    if product["reviews"] > 500:
        score += 2

    if product["reviews"] > 5000:
        score -= 3

    # Profit
    profit = product["selling_price"] - product["cost"]
    margin = profit / product["cost"]

    product["profit"] = round(profit, 2)
    product["margin"] = round(margin, 2)

    if margin > 0.5:
        score += 3

    product["score"] = score

    return product


def is_winner(product):
    if product["margin"] > 0.5 and product["rating"] >= 4.2:
        return True

    return product["score"] >= 11