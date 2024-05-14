import os
import sqlite3

from dotenv import load_dotenv


load_dotenv()

DB_NAME = os.getenv("DB_NAME")


def get_database_connection() -> sqlite3.Connection:
    con = sqlite3.connect(DB_NAME)

    return con
