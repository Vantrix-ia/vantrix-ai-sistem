from vantrix_proyet.engine.feature_engine import analyze_product
from vantrix_proyet.engine.gap_engine import evaluate_opportunity
from vantrix_proyet.engine.financial_engine import calculate_financials
from vantrix_proyet.engine.decision_engine import calculate_v_score, make_decision
from database import create_tables, save_product, get_all_products


def run_pipeline():

    create_tables()

    products = [
        "Ice facial roller",
        "Magnetic car phone holder",
        "Sunset lamp"
    ]

    results = []

    for product in products:

        features = analyze_product(product)

        opportunity = evaluate_opportunity(features)
        financials = calculate_financials(opportunity)

        v_score = calculate_v_score(
            financials,
            features["supplier_score"],
            features["market_fatigue"],
            features["entry_barrier"]
        )

        decision = make_decision(v_score)

        result = {
            "product": product,
            "opportunity": opportunity,
            "profit": financials["profit"],
            "margin": financials["margin"],
            "v_score": v_score,
            "decision": decision
        }

        save_product(result)

        results.append(result)

        print(f"✅ RESULT: {result}")

    print("\n🔥 FINAL SUMMARY:")
    for r in results:
        print(r)

    history = get_all_products()

    print("\n📊 LEARNING DATA:")
    for h in history[:5]:
        print(h)


if __name__ == "__main__":
    run_pipeline()