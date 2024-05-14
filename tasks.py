import os
from datetime import datetime
import pytz
from celery import Celery
from celery.schedules import crontab
from dotenv import load_dotenv

from database.load_data_to_db import populate_table
from parser.xpath_parser import get_exchange_rate


load_dotenv()

DB_NAME = os.getenv("DB_NAME")
TIME_ZONE = os.getenv("TIME_ZONE")

app = Celery("tasks", broker="redis://redis:6379")
app.conf.broker_connection_retry_on_startup = True

app.conf.timezone = TIME_ZONE
app.conf.beat_schedule = {
    "update-exchange-rate": {
        "task": "tasks.parse_exchange_rate",
        "schedule": crontab(minute="0", hour="*"),
    },
}


@app.task(bind=True)
def parse_exchange_rate(self):
    exchange_rate = get_exchange_rate()

    tz = pytz.timezone(TIME_ZONE)
    current_time = datetime.now(tz=tz)

    populate_table(time=current_time, exchange_rate=exchange_rate)

    return f"Exchange rate {exchange_rate} was saved at {current_time}."
