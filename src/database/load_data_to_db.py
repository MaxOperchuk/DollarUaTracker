import os
from datetime import datetime

from dotenv import load_dotenv

from src.database.connect_db import get_database_connection


load_dotenv()

TABLE_NAME = os.getenv("TABLE_NAME")


def populate_table(time: datetime, exchange_rate: float) -> None:

    add_data_query = f"""
        INSERT INTO {TABLE_NAME} 
        (date, usd_to_uah) VALUES (?, ?);
    """

    conn = get_database_connection()
    conn.execute(add_data_query, (time, exchange_rate))
    conn.commit()
    conn.close()
