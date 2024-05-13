import os
import sqlite3

from dotenv import load_dotenv


load_dotenv()

DB_NAME = os.getenv("DB_NAME")
ABS_PATH_TO_PROJECT_DIR = os.getenv("ABS_PATH_TO_PROJECT_DIR")


def get_database_connection() -> sqlite3.Connection:
    os.chdir(ABS_PATH_TO_PROJECT_DIR)
    con = sqlite3.connect(os.path.abspath(DB_NAME))

    return con
