import json
import os
from datetime import datetime

DB_FILE = "winners.json"


def load_winners():
    if not os.path.exists(DB_FILE):
        with open(DB_FILE, "w", encoding="utf-8") as f:
            json.dump([], f)
        return []

    try:
        with open(DB_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except:
        return []


def save_winner(product):
    data = load_winners()

    product_title = product.get("title") or product.get("name")

    if not product_title:
        return False

    if any((p.get("title") or p.get("name")) == product_title for p in data):
        return False

    product["timestamp"] = datetime.now().isoformat()

    data.append(product)

    with open(DB_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    return True