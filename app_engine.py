from fastapi import FastAPI
from sqlalchemy import create_engine, text

app = FastAPI()

DATABASE_URL = "sqlite:///test.db"
engine = create_engine(DATABASE_URL)


@app.get("/")
def home():
    return {"status": "Vantrix backend activo"}


@app.get("/products")
def get_products():
    with engine.connect() as conn:
        result = conn.execute(text("SELECT * FROM products"))
        return [dict(row._mapping) for row in result]


@app.get("/winners")
def get_winners():
    with engine.connect() as conn:
        result = conn.execute(text("""
            SELECT * FROM products
            WHERE v_score >= 9
            ORDER BY v_score DESC
        """))
        return [dict(row._mapping) for row in result]


@app.get("/stats")
def stats():
    with engine.connect() as conn:
        total = conn.execute(
            text("SELECT COUNT(*) FROM products")
        ).scalar()

        winners = conn.execute(
            text("SELECT COUNT(*) FROM products WHERE v_score >= 9")
        ).scalar()

        return {
            "total_products": total,
            "winners": winners
        }