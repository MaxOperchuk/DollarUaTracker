import os

from dotenv import load_dotenv
from openpyxl import Workbook


load_dotenv()

FILE_NAME = os.getenv("FILE_NAME")


def write_to_xlsx(data: list) -> None:
    wb = Workbook()
    ws = wb.active

    for row in data:
        ws.append(row)

    wb.save(FILE_NAME)
