from database.connect_db import get_database_connection


def create_table() -> None:
    authors_table_creation_query = (
        """CREATE TABLE IF NOT EXISTS 
        exchange_rates(date TEXT, usd_to_uah FLOAT)"""
    )

    con = get_database_connection()
    con.execute(authors_table_creation_query)
    con.close()
