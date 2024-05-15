import os

import httpx
from dotenv import load_dotenv
from tenacity import (
    retry,
    stop_after_attempt,
    wait_fixed,
    retry_if_exception_type
)


load_dotenv()

URL = os.getenv("RATE_URL")


@retry(
    stop=stop_after_attempt(5),
    wait=wait_fixed(1),
    retry=retry_if_exception_type(httpx.ConnectError),
)
def get_response():
    client = httpx.Client()
    response = client.get(URL)

    return response.content
