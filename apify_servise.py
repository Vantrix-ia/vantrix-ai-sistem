import os
from apify_client import ApifyClient
from dotenv import load_dotenv

# Cargar .env
load_dotenv()

APIFY_TOKEN = os.getenv("APIFY_TOKEN")

if not APIFY_TOKEN:
    raise ValueError("❌ APIFY_TOKEN no está configurado en .env")

client = ApifyClient(APIFY_TOKEN)


def run_actor(actor_id, input_data):
    print(f"\n🚀 Ejecutando actor: {actor_id}")
    print(f"📦 Input: {input_data}")

    try:
        run = client.actor(actor_id).call(run_input=input_data)

        dataset_id = run.get("defaultDatasetId")

        if not dataset_id:
            print("⚠️ No se encontró dataset")
            return []

        items = list(client.dataset(dataset_id).iterate_items())

        print(f"✅ Items obtenidos: {len(items)}")

        return items

    except Exception as e:
        print("❌ Error ejecutando Apify:", str(e))
        return []