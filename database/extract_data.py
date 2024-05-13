import os

from dotenv import load_dotenv

from database.connect_db import get_database_connection


load_dotenv()

TABLE_NAME = os.getenv("TABLE_NAME")


def fetch_data():
    conn = get_database_connection()
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM {TABLE_NAME}")

    rows = cursor.fetchall()
    conn.close()

    return rows
