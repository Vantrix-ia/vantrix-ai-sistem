from vantrix_proyet.worker.pipeline import run_pipeline
from vantrix_proyet.automation.whatsapp_sender import send_whatsapp_message


def run_daily():
    trend = "portable blender"

    results = run_pipeline(trend)

    winners = [r for r in results if r["decision"] == "BUY"]

    if not winners:
        send_whatsapp_message("❌ No winners today")
        return

    message = "🔥 WINNERS DEL DÍA:\n\n"

    for w in winners[:5]:
        message += f"{w['title']}\n💰 Profit: {w['profit']}\n⭐ Score: {w['v_score']}\n\n"

    send_whatsapp_message(message)


if __name__ == "__main__":
    run_daily()