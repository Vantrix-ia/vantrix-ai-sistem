import json
import os

FILE_PATH = "vantrix_proyet/data/sent_products.json"


def load_sent_products():
    if not os.path.exists(FILE_PATH):
        return set()

    try:
        with open(FILE_PATH, "r") as f:
            data = json.load(f)
            return set(data)
    except:
        return set()


def save_sent_products(products):
    try:
        with open(FILE_PATH, "w") as f:
            json.dump(list(products), f, indent=2)
    except Exception as e:
        print("❌ ERROR GUARDANDO MEMORIA:", e)