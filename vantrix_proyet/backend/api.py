from fastapi import FastAPI
import sqlite3

app = FastAPI()


DB_PATH = "vantrix.db"


def get_connection():
    return sqlite3.connect(DB_PATH)


@app.get("/")
def home():
    return {"status": "Vantrix AI running 🚀"}


@app.get("/products")
def get_products():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT title, profit, v_score, decision FROM products")
    rows = cursor.fetchall()

    conn.close()

    return [
        {
            "title": r[0],
            "profit": r[1],
            "score": r[2],
            "decision": r[3],
        }
        for r in rows
    ]