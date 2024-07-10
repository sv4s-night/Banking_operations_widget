"""
1. Реализуйте функцию, которая принимает на вход путь до JSON-файла и возвращает список словарей с данными о
финансовых транзакциях. Если файл пустой, содержит не список или не найден, функция возвращает пустой список.

"""


""" Путь до Json файла
https://drive.google.com/file/d/1C0bUdTxUhck-7BoqXSR1wIEp33BH5YXy/view
"""


import json


def read_financial_transactions(file_path: str) -> list:     # функция принимает путь до файла
    """Функция возвращает список словарей с данными о финансовых транзакциях"""
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            if isinstance(data, list):
                return data
            else:
                return []
    except (FileNotFoundError, json.JSONDecodeError):
        return []


# Example Usage
file_path = 'data/operations.json'          # путь до json файла
transactions = read_financial_transactions(file_path)
print(transactions)




def convert_transaction_to_rub(transaction: float) -> float:
    """Функция возвращает сумму транзакции в Рублях"""
    if transaction['currency'] == 'RUB':
        return transaction['amount']
    else:
        converted_amount = transaction['amount']  # Placeholder for conversion logic (обращение к функции конвертации)
        return converted_amount


