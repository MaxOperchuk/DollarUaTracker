import os

import requests
from dotenv import load_dotenv
from lxml import html


load_dotenv()

URL = os.getenv("RATE_URL")
RATE_SEARCH_PATTERN = "//div[@jsname='LXPcOd']//div[@jsname='ip75Cb']/div/text()"


def get_exchange_rate() -> float:
    response = requests.get(URL)
    html_content = response.text
    tree = html.fromstring(html_content)

    rate = tree.xpath(RATE_SEARCH_PATTERN)

    return float(rate[0])
