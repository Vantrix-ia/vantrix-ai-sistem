from vantrix_proyet.core.logger import logger
from vantrix_proyet.core.decision_expert import VantrixDecisionExpert

from vantrix_proyet.engine.feature_engine import analyze_product
from vantrix_proyet.engine.scorer import calculate_scores

from vantrix_proyet.services.database import save_product
from vantrix_proyet.core.stealth_scraper import get_products


def run_pipeline(trend="viral product"):

    logger.info(f"🚀 Iniciando pipeline para: {trend}")

    # 1. Scraping
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

    # 2. Procesamiento
    for p in products:

        try:
            # 🔹 Step 1: convertir a modelo Product
            product = analyze_product(p)

            # 🔹 Step 2: scoring adicional (trend, saturation, etc.)
            product = calculate_scores(product)

            # 🔹 Step 3: decisión
            product = expert.make_decision(product)

            # 🔹 Log
            logger.info(
                f"🧠 {product.title} | Profit: {product.profit:.2f} | "
                f"VScore: {product.v_score:.2f} | Decision: {product.decision}"
            )

            # 🔹 Guardar en DB
            save_product(product)

        except Exception as e:
            logger.error(f"❌ Error procesando producto: {e}")

    logger.info("✅ Pipeline finalizado")