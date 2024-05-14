import os
import sys

from dotenv import load_dotenv

sys.path.insert(
    0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
)

from database.connect_db import get_database_connection


load_dotenv()

TABLE_NAME = os.getenv("TABLE_NAME")


def create_table() -> None:
    authors_table_creation_query = (
        f"""
        CREATE TABLE IF NOT EXISTS 
        {TABLE_NAME}(date TEXT, usd_to_uah FLOAT)
        """
    )

    con = get_database_connection()
    con.execute(authors_table_creation_query)
    con.close()


if __name__ == "__main__":
    create_table()
