from vantrix_proyet.core.logger import logger

# 🔥 MODO SIMPLE (sin Twilio para evitar errores ahora)
# Luego lo activamos bien si quieres producción real

def send_whatsapp(product: dict):

    try:
        # 📲 Simulación de envío
        logger.info("📲 WhatsApp enviado (simulado)")
        logger.info(
            f"🔥 ALERTA:\n"
            f"Producto: {product['title']}\n"
            f"Precio: {product['selling_price']}\n"
            f"Score: {product.get('score', 0)}\n"
            f"Decision: {product['decision']}"
        )

    except Exception as e:
        logger.error(f"❌ Error en notifier: {e}")