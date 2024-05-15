import os

from dotenv import load_dotenv
from openpyxl import Workbook
from openpyxl.styles import Font

load_dotenv()

FILE_NAME = os.getenv("FILE_NAME")
COLUMN_NAMES = ["datetime", "exchange_rate"]


def write_to_xlsx(data: list) -> None:
    wb = Workbook()
    ws = wb.active

    ws.append(COLUMN_NAMES)
    header_row = ws[1]

    for cell in header_row:
        cell.font = Font(bold=True)

    for row in data:
        ws.append(row)

    wb.save(FILE_NAME)
