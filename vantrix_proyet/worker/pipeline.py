from vantrix_proyet.core.stealth_scraper import get_products
from vantrix_proyet.engine.scorer import calculate_v_score
from vantrix_proyet.services.notifier import notify
from vantrix_proyet.core.memory import load_sent_products, save_sent_products


def run_pipeline(trend="portable blender"):
    print("\n🚀 INICIANDO PIPELINE VANTRIX\n")

    sent_products = load_sent_products()

    try:
        products = get_products(trend)
        print(f"📦 Productos encontrados: {len(products)}")
    except Exception as e:
        print("❌ ERROR SCRAPER:", e)
        return

    if not products:
        print("⚠️ No hay productos")
        return

    results = []
    new_sent = set(sent_products)

    for p in products:
        title = p.get("title")

        # 🚫 EVITAR REPETIDOS
        if title in sent_products:
            print(f"⏭️ Ya enviado: {title}")
            continue

        try:
            print(f"🔍 Analizando: {title}")

            score = calculate_v_score(p)

            if score >= 5:
                results.append({
                    "title": title,
                    "price": p.get("selling_price"),
                    "score": score
                })

                new_sent.add(title)

        except Exception as e:
            print("❌ ERROR SCORING:", e)

    if not results:
        print("⚠️ No hay nuevas oportunidades")
        return

    # Ordenar
    results = sorted(results, key=lambda x: x["score"], reverse=True)
    top = results[:3]

    # Mensaje
    message = "🚀 VANTRIX ALERT\n\nNuevas oportunidades:\n\n"

    for i, r in enumerate(top, 1):
        message += (
            f"{i}. {r['title']}\n"
            f"💰 Precio: ${r['price']}\n"
            f"⭐ Score: {r['score']}\n\n"
        )

    print("\n📲 Enviando resumen...")
    notify(message)

    # 💾 GUARDAR MEMORIA
    save_sent_products(new_sent)