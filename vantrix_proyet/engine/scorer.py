def calculate_v_score(product):
    """
    Score inteligente estilo IA basado en:
    - demanda
    - margen
    - tendencia
    - confianza
    """

    try:
        # =========================
        # INPUTS
        # =========================
        price = product.get("selling_price", 0)
        cost = product.get("cost", 0)
        rating = product.get("rating", 0)
        reviews = product.get("reviews", 0)
        trend = product.get("trend_score", 0)

        # =========================
        # 1. MARGEN
        # =========================
        if cost == 0:
            margin_score = 0
        else:
            margin = (price - cost) / cost

            if margin > 2:
                margin_score = 10
            elif margin > 1:
                margin_score = 8
            elif margin > 0.5:
                margin_score = 6
            else:
                margin_score = 3

        # =========================
        # 2. DEMANDA (REVIEWS)
        # =========================
        if reviews > 1000:
            demand_score = 10
        elif reviews > 300:
            demand_score = 8
        elif reviews > 100:
            demand_score = 6
        elif reviews > 50:
            demand_score = 4
        else:
            demand_score = 2

        # =========================
        # 3. CALIDAD (RATING)
        # =========================
        if rating >= 4.7:
            quality_score = 10
        elif rating >= 4.5:
            quality_score = 8
        elif rating >= 4.2:
            quality_score = 6
        else:
            quality_score = 3

        # =========================
        # 4. TENDENCIA
        # =========================
        trend_score = min(trend, 10)

        # =========================
        # 5. RIESGO
        # =========================
        risk_penalty = 0

        if rating < 4.2:
            risk_penalty += 2

        if reviews < 50:
            risk_penalty += 2

        if margin_score < 5:
            risk_penalty += 2

        # =========================
        # 6. SCORE FINAL
        # =========================
        score = (
            margin_score * 0.3 +
            demand_score * 0.25 +
            quality_score * 0.2 +
            trend_score * 0.25
        ) - risk_penalty

        return round(score, 2)

    except Exception as e:
        print("❌ ERROR SCORER:", e)
        return 0