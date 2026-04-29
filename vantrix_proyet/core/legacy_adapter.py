from vantrix_proyet.engine.feature_engine import analyze_product
from vantrix_proyet.engine.gap_engine import evaluate_opportunity
from vantrix_proyet.engine.financial_engine import calculate_financials
from vantrix_proyet.engine.decision_engine import calculate_v_score


def run_legacy_analysis(product_name: str):
    try:
        features = analyze_product(product_name)
        opportunity = evaluate_opportunity(features)
        financials = calculate_financials(opportunity)
        v_score = calculate_v_score(financials)

        return {
            "title": product_name,
            "cost": financials.get("cost", 10),
            "selling_price": financials.get("price", 25),
            "rating": features.get("rating", 4.5),
            "reviews": features.get("reviews", 100),
            "v_score": v_score,
            "profit": financials.get("profit", 10)
        }

    except Exception as e:
        print("⚠️ Error en legacy engine:", e)
        return None