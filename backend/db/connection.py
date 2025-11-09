import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

def get_connection():
    try:
        conn = psycopg2.connect(
            dbname=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            host=os.getenv("DB_HOST"),
            port=os.getenv("DB_PORT")
        )
        return conn
    except Exception as e:
        print(" Database connection error:", e)
        return None


def execute_query(query, params=None, fetch=False):
    conn = get_connection()
    if not conn:
        return None

    try:
        cur = conn.cursor()
        cur.execute(query, params)
        data = cur.fetchall() if fetch else None
        conn.commit()
        cur.close()
        conn.close()
        return data
    except Exception as e:
        print(" Query Error:", e)
        conn.close()
        return None
