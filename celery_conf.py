import os

from celery import Celery
from celery.schedules import crontab
from dotenv import load_dotenv


load_dotenv()

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
