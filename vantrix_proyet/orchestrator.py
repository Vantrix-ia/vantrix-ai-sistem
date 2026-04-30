class VantrixEngine:

    def run(self, products):
        results = []

        for product in products:
            cost = product["cost"]
            price = product["selling_price"]
            rating = product["rating"]
            reviews = product["reviews"]
            trend = product["trend_score"]

            profit = price - cost
            margin = profit / cost if cost > 0 else 0

            margin_score = min(margin * 10, 10)
            trend_score = trend
            saturation_score = max(0, 10 - (reviews / 300))
            branding_score = rating * 2

            v_score = (
                margin_score * 0.4 +
                trend_score * 0.3 +
                saturation_score * 0.2 +
                branding_score * 0.1
            )

            if v_score >= 8:
                decision = "BUY"
            elif v_score >= 6:
                decision = "TEST"
            else:
                decision = "SKIP"

            results.append({
                "title": product["title"],
                "cost": cost,
                "selling_price": price,
                "profit": round(profit, 2),
                "margin": round(margin, 2),
                "rating": rating,
                "reviews": reviews,
                "trend_score": trend,
                "v_score": round(v_score, 2),
                "decision": decision
            })

        return results