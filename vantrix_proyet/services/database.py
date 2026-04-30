import json
from vantrix_proyet.core.logger import logger

def save_product(product):
    data = product.to_dict()

    try:
        with open("winners.json", "a", encoding="utf-8") as f:
            f.write(json.dumps(data) + "\n")

        logger.info(f"💾 Guardado: {product.title}")

    except Exception as e:
        logger.error(f"Error guardando producto: {e}")