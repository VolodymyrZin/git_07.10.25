import psycopg2
import os

def get_connection():
    return psycopg2.connect(
        dbname=os.getenv("POSTGRES_DB", "apple_store"),
        user=os.getenv("POSTGRES_USER", "postgres"),
        password=os.getenv("POSTGRES_PASSWORD", "1"),
        host=os.getenv("POSTGRES_HOST", "apple_store"),
        port=os.getenv("POSTGRES_PORT", "5432"),
    )
