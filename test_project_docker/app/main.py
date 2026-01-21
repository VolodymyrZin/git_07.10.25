from app.db import get_connection

def create_table():
    with get_connection() as conn, conn.cursor() as cur:
        cur.execute("""
            CREATE TABLE IF NOT EXISTS products (
                id SERIAL PRIMARY KEY,
                name TEXT NOT NULL,
                price INTEGER NOT NULL
            );
        """)
        conn.commit()

def insert_product(name, price):
    with get_connection() as conn, conn.cursor() as cur:
        cur.execute(
            "INSERT INTO products (name, price) VALUES (%s, %s) RETURNING id;",
            (name, price)
        )
        conn.commit()
        return cur.fetchone()[0]

def update_product(product_id, price):
    with get_connection() as conn, conn.cursor() as cur:
        cur.execute(
            "UPDATE products SET price=%s WHERE id=%s;",
            (price, product_id)
        )
        conn.commit()

def delete_product(product_id):
    with get_connection() as conn, conn.cursor() as cur:
        cur.execute("DELETE FROM products WHERE id=%s;", (product_id,))
        conn.commit()

def get_products():
    with get_connection() as conn, conn.cursor() as cur:
        cur.execute("SELECT name, price FROM products;")
        return cur.fetchall()