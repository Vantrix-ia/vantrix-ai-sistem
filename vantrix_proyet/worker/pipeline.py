from vantrix_proyet.core.logger import logger
from vantrix_proyet.core.decision_expert import VantrixDecisionExpert

from vantrix_proyet.engine.feature_engine import analyze_product
from vantrix_proyet.engine.scorer import calculate_scores

from vantrix_proyet.services.database import save_product
from vantrix_proyet.services.notifier import send_whatsapp

from vantrix_proyet.core.stealth_scraper import get_products


def run_pipeline(trend="viral product"):

    logger.info(f"🚀 Iniciando pipeline para: {trend}")

    # 🔎 1. SCRAPING
    try:
        products = get_products(trend)
        logger.info(f"📦 Productos encontrados: {len(products)}")
    except Exception as e:
        logger.error(f"❌ Error en scraper: {e}")
        return

    if not products:
        logger.warning("⚠️ No hay productos")
        return

    expert = VantrixDecisionExpert()

    # ⚙️ 2. PROCESAMIENTO
    for p in products:

        try:
            # 🧠 Paso 1: análisis base
            product = analyze_product(p)

            # 📊 Paso 2: scoring
            product = calculate_scores(product)

            # 🎯 Paso 3: decisión
            product = expert.make_decision(product)

            # 📋 LOG
            logger.info(
                f"📦 {product['title']} | Score: {product.get('score', 0)} | Decision: {product['decision']}"
            )

            # 💾 + 📲 SOLO WINNERS
            if product["decision"] == "WINNER":
                save_product(product)
                send_whatsapp(product)

        except Exception as e:
            logger.error(f"❌ Error procesando producto: {e}")

    logger.info("✅ Pipeline finalizado")