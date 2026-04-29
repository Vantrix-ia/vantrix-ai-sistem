from data.source import get_products
from vantrix_proyet.engine.scorer import calculate_v_score
from vantrix_proyet.services.notifier import notify

def run_pipeline():
    products = get_products()

    # calcular score
    for p in products:
        p["v_score"] = calculate_v_score(p)

    # ordenar
    products.sort(key=lambda x: x["v_score"], reverse=True)

    # lógica de alertas
    alerts = [
        p for p in products
        if p["v_score"] > 12 and p["rating"] >= 4.2 and p["reviews"] > 100
    ]

    # disparar notificaciones
    notify(alerts)

    return {
        "products": products,
        "alerts": alerts
    }