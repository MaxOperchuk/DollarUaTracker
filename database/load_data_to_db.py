from datetime import datetime

from database.connect_db import get_database_connection
from database.create_db import create_table


def populate_table(exchange_rate: float) -> None:

    create_table()

    add_data_query = """
        INSERT INTO exchange_rates 
        (date, usd_to_uah) VALUES (?, ?);
    """

    con = get_database_connection()
    con.execute(add_data_query, (datetime.now(), exchange_rate))
    con.commit()
    con.close()
