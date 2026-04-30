from dataclasses import dataclass


@dataclass
class Product:
    title: str
    cost: float
    selling_price: float = 0
    profit: float = 0
    margin: float = 0
    v_score: float = 0
    decision: str = "UNKNOWN"