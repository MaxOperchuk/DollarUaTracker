import os
from datetime import datetime

import pytz
from dotenv import load_dotenv

from celery_conf import app
from src.database.load_data_to_db import populate_table
from src.parser.xpath_parser import get_exchange_rate


load_dotenv()

DB_NAME = os.getenv("DB_NAME")
TIME_ZONE = os.getenv("TIME_ZONE")


@app.task(bind=True)
def parse_exchange_rate(self):
    exchange_rate = get_exchange_rate()

    tz = pytz.timezone(TIME_ZONE)
    current_time = datetime.now(tz=tz)

    populate_table(time=current_time, exchange_rate=exchange_rate)

    return f"Exchange rate {exchange_rate} was saved at {current_time}."
