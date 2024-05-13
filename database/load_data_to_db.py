import os
from datetime import datetime

from dotenv import load_dotenv

from database.connect_db import get_database_connection
from database.create_db import create_table


load_dotenv()

TABLE_NAME = os.getenv("TABLE_NAME")


def populate_table(time: datetime, exchange_rate: float) -> None:
    create_table()

    add_data_query = f"""
        INSERT INTO {TABLE_NAME} 
        (date, usd_to_uah) VALUES (?, ?);
    """

    conn = get_database_connection()
    conn.execute(add_data_query, (time, exchange_rate))
    conn.commit()
    conn.close()
