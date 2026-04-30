def calculate_scores(product: dict):

    try:
        # 💰 Profit
        profit = product["selling_price"] - product["cost"]
        margin = profit / product["cost"]

        # 📊 Score simple
        score = 0

        if margin > 0.5:
            score += 5
        elif margin > 0.3:
            score += 3

        if product.get("rating", 0) >= 4.5:
            score += 3
        elif product.get("rating", 0) >= 4.0:
            score += 2

        if product.get("reviews", 0) > 1000:
            score += 2
        elif product.get("reviews", 0) > 500:
            score += 1

        # 🔥 Guardar en dict (NO objeto)
        product["profit"] = round(profit, 2)
        product["margin"] = round(margin, 2)
        product["score"] = score

        return product

    except Exception as e:
        raise Exception(f"Error en scorer: {e}")