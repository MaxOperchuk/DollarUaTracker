from openpyxl import Workbook


def write_to_xlsx(data):
    wb = Workbook()
    ws = wb.active

    for row in data:
        ws.append(row)

    wb.save("exchange_rates.xlsx")
