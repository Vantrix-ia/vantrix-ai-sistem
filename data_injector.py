from sqlalchemy import create_engine, text
from aliexpress_scraper import get_products

DATABASE_URL = "sqlite:///test.db"
engine = create_engine(DATABASE_URL)

def insert_products():
    products = get_products()

    with engine.connect() as conn:
        for p in products:
            conn.execute(text("""
                INSERT INTO products 
                (name, price, rating, reviews, profit, margin, v_score, decision, trend_source)
                VALUES (:name, :price, :rating, :reviews, :profit, :margin, :v_score, :decision, :trend_source)
            """), p)

        conn.commit()

    print("Productos insertados correctamente")

if __name__ == "__main__":
    insert_products()