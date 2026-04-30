import math
from datetime import datetime


# 🔥 velocidad de crecimiento (clave real)
def calculate_velocity(current, previous):
    if previous == 0:
        return 0
    return (current - previous) / previous


# 🔥 aceleración (lo que detecta virales antes de explotar)
def calculate_acceleration(v1, v2):
    return v2 - v1


# 🔥 score predictivo real
def predictive_score(reviews_history):
    """
    reviews_history = [r_t-2, r_t-1, r_t]
    """

    if len(reviews_history) < 3:
        return 0

    v1 = calculate_velocity(reviews_history[1], reviews_history[0])
    v2 = calculate_velocity(reviews_history[2], reviews_history[1])

    accel = calculate_acceleration(v1, v2)

    # modelo simple pero brutal
    score = (v2 * 5) + (accel * 10)

    return round(score, 2)


# 🔥 clasificación real de oportunidad
def classify_opportunity(score):
    if score > 5:
        return "🔥 EARLY VIRAL"
    elif score > 2:
        return "🚀 TREND RISING"
    elif score > 0.5:
        return "🟡 STABLE"
    else:
        return "❌ DEAD"


# 🔥 simulación temporal (hasta tener datos reales históricos)
def simulate_history(reviews):
    """
    Simula crecimiento pasado para MVP
    """
    return [
        int(reviews * 0.6),
        int(reviews * 0.8),
        reviews
    ]