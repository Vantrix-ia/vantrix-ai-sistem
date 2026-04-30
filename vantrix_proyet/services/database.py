import sqlite3
import os

# 📁 ruta base del proyecto
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 📁 archivo DB
DB_PATH = os.path.join(BASE_DIR, "data", "vantrix.db")


def init_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT,
        profit REAL,
        v_score REAL,
        decision TEXT
    )
    """)

    conn.commit()
    conn.close()


def save_product(product):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO products (title, profit, v_score, decision)
    VALUES (?, ?, ?, ?)
    """, (
        product.title,
        product.profit,
        product.v_score,
        product.decision
    ))

    conn.commit()
    conn.close()