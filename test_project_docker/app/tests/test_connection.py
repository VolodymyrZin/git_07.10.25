import os
import psycopg2

def test_connection():
    conn = psycopg2.connect(
        dbname=os.getenv("POSTGRES_DB", "apple_store"),
        user=os.getenv("POSTGRES_USER", "postgres"),
        password=os.getenv("POSTGRES_PASSWORD", "1"),
        host=os.getenv("POSTGRES_HOST", "apple_store"),
        port=os.getenv("POSTGRES_PORT", "5432"),
    )
    cur = conn.cursor()
    cur.execute("SELECT 'apple';")
    result = cur.fetchone()
    assert result[0] == 'apple'
    conn.close()
