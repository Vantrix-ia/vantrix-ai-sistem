import json

DB_FILE = "winners.json"


def analyze_performance():
    try:
        with open(DB_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
    except:
        print("⚠️ No hay datos")
        return

    if not data:
        print("⚠️ Sin winners aún")
        return

    total = len(data)

    avg_score = sum(p.get("score", 0) for p in data) / total
    avg_margin = sum(p.get("margin", 0) for p in data) / total
    avg_rating = sum(p.get("rating", 0) for p in data) / total

    print("\n📊 ANÁLISIS")
    print(f"Productos: {total}")
    print(f"Score promedio: {round(avg_score,2)}")
    print(f"Margin promedio: {round(avg_margin,2)}")
    print(f"Rating promedio: {round(avg_rating,2)}")