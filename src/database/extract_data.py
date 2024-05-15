import os
from datetime import datetime

import pytz
from dotenv import load_dotenv

from src.database.connect_db import get_database_connection

load_dotenv()

TABLE_NAME = os.getenv("TABLE_NAME")
TIME_ZONE = os.getenv("TIME_ZONE")


def fetch_data():
    conn = get_database_connection()
    cursor = conn.cursor()

    tz = pytz.timezone(TIME_ZONE)
    current_date = datetime.now(tz=tz).date()

    cursor.execute(
        f"SELECT * FROM {TABLE_NAME} "
        f"WHERE date LIKE '{current_date}%'"
    )

    rows = cursor.fetchall()
    conn.close()

    return rows
