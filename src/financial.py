import csv

import pandas as pd


def reader_file_transaction_csv(file_path: str) -> list[dict]:
    """Функция считывающая cvs файл и возвращающая список словарей (HW lesson 13.1)"""
    with open(file_path, "r", encoding="utf-8") as file:
        data_frame = csv.reader(file, delimiter=";")
        header = next(data_frame)
        result = []
        for row in data_frame:
            row_dict = {
                "id": row[header.index("id")],
                "state": row[header.index("state")],
                "date": row[header.index("date")],
                "operationAmount": {
                    "amount": row[header.index("amount")],
                    "currency": {
                        "name": row[header.index("currency_name")],
                        "code": row[header.index("currency_code")],
                    },
                },
                "description": row[header.index("description")],
                "from": row[header.index("from")],
                "to": row[header.index("to")],
            }
            result.append(row_dict)

    return result


def reader_file_transaction_excel(file_path: str) -> list[dict]:
    """Функция считывающая файл в формате excel и возвращающая список словарей (HW lesson 13.1)"""
    data_frame = pd.read_excel(file_path)
    result = []
    rows_count = len(data_frame)
    for i in range(0, rows_count):
        row_dict = {
            "id": data_frame.at[i, "id"],
            "state": data_frame.at[i, "state"],
            "date": data_frame.at[i, "date"],
            "operationAmount": {
                "amount": data_frame.at[i, "amount"],
                "currency": {
                    "name": data_frame.at[i, "currency_name"],
                    "code": data_frame.at[i, "currency_code"],
                },
            },
            "description": data_frame.at[i, "description"],
            "from": data_frame.at[i, "from"],
            "to": data_frame.at[i, "to"],
        }
        result.append(row_dict)
    return result
