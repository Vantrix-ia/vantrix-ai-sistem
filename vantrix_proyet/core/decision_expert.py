class VantrixDecisionExpert:

    def evaluate(self, product):
        cost = product.get("cost", 0)
        price = product.get("selling_price", 0)
        rating = product.get("rating", 0)
        reviews = product.get("reviews", 0)
        trend = product.get("trend_score", 0)

        # 🧮 PROFIT REAL
        profit = price - cost

        # 📊 MARGEN NORMALIZADO
        margin = profit / cost if cost > 0 else 0

        # ⭐ SCORE COMPONENTES (normalizados)
        margin_score = min(margin * 10, 10)           # max 10
        trend_score = trend                           # ya viene 0–10
        saturation_score = max(0, 10 - (reviews / 300))
        branding_score = rating * 2                  # rating 5 → 10

        # 🧠 V-SCORE FINAL
        v_score = (
            margin_score * 0.4 +
            trend_score * 0.3 +
            saturation_score * 0.2 +
            branding_score * 0.1
        )

        # 🎯 DECISIÓN
        if v_score >= 8:
            decision = "BUY"
        elif v_score >= 6:
            decision = "TEST"
        else:
            decision = "SKIP"

        # ✅ OUTPUT COMPLETO (CLAVE DEL FIX)
        return {
            "title": product.get("title"),
            "cost": cost,
            "selling_price": price,
            "profit": round(profit, 2),
            "margin": round(margin, 2),
            "rating": rating,
            "reviews": reviews,
            "trend_score": trend,
            "v_score": round(v_score, 2),
            "decision": decision
        }