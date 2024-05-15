import os

import tenacity
from bs4 import BeautifulSoup
from dotenv import load_dotenv

from src.parser.request import get_response


load_dotenv()

URL = os.getenv("RATE_URL")
RATE_SEARCH_PATTERN = (
    "c-wiz:nth-of-type(2) > div > div:nth-of-type(4) "
    "> div > main > div:nth-of-type(2) > div > c-wiz "
    "> div > div > div > div > div > div > div > span > div"
)


def get_exchange_rate() -> float:

    try:
        response_content = get_response()
    except tenacity.RetryError:
        return 0

    soup = BeautifulSoup(response_content, "html.parser")

    rate = soup.select_one(RATE_SEARCH_PATTERN).text

    return float(rate)
