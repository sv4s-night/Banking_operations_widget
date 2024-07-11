""" Путь до Json файла
https://drive.google.com/file/d/1C0bUdTxUhck-7BoqXSR1wIEp33BH5YXy/view
"""

import json
import requests
# from src.external_api import convert


def read_financial_transactions(path):     # функция принимает путь до файла
    """Функция возвращает список словарей с данными о финансовых транзакциях"""
    try:
        with open(path, 'r', encoding="UTF-8") as file:
            data = json.load(file)
            if isinstance(data, list):
                return data
            else:
                return []
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def convert(to, val_from, amount):
    """Обращение к API"""
    url = f"https://api.apilayer.com/exchangerates_data/convert?to={to}&from={val_from}&amount={amount}"

    payload = {}
    headers = {
        "apikey": "sctfncfS2MC1onu8cMTgSxeEqFY0FZBy"
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    # status_code = response.status_code
    result = response.text
    return result


def proverka(transactions):
    """Функция проверки явл ли Рублем"""
    tor = "RUB"
    valute_from = transactions[0]["operationAmount"]["currency"]["code"]
    amount = transactions[0]["operationAmount"]["amount"]

    if valute_from != "RUB":
        # API
        exchange_rate = convert(tor, valute_from, amount)
        # amount_rubles = transactions["amount"] * exchange_rate
        return exchange_rate
    else:
        return amount



# def convert_transaction_to_rub(transaction: float) -> float:
#     """Функция возвращает сумму транзакции в Рублях"""
#     if transaction['currency'] == 'RUB':
#         return transaction['amount']
#     else:
#         converted_amount = transaction['amount']  # Placeholder for conversion logic (обращение к функции конвертации)
#         return converted_amount


# def extract_transaction_amount(transaction):
#     amount = float(transaction[0]["operationAmount"]["amount"])
#     if transaction[0]["operationAmount"]["currency"]["code"] in ["USD", "EUR"]:
#         # Call external API to get currency exchange rate and convert amount to rubles
#         # Conversion logic here
#         pass
#     return amount
#
#
#
#
#     valute_from = "USD"
#     valute_to = "RUS"
#     amount = 10
#
#     # url = "https://api.apilayer.com/exchangerates_data/convert?to={to}&from={from}&amount={amount}"
#     url = f"https://api.apilayer.com/exchangerates_data/convert?to={valute_to}&from={valute_from}&amount={amount}"
#
#     payload = {}
#     headers = {
#         "apikey": "sctfncfS2MC1onu8cMTgSxeEqFY0FZBy"
#     }
#     response = requests.request("GET", url, headers=headers, data=payload)
#
#     status_code = response.status_code
#     result = response.text



# def extract_transaction_amount(transaction):
#     amount = float(transaction[0]["operationAmount"]["amount"])
#     valute = transaction[0]["operationAmount"]["currency"]["code"]
#     valute_to = "RUS"
#     if valute in ["USD", "EUR"]:
#         # Call external API to get currency exchange rate and convert amount to rubles
#         # Conversion logic here
#         pass
#     #=========================
#     url = f"https://api.apilayer.com/exchangerates_data/convert?to={valute_to}&from={valute}&amount={amount}"
#
#     payload = {}
#     headers = {
#         "apikey": "sctfncfS2MC1onu8cMTgSxeEqFY0FZBy"
#     }
#     response = requests.request("GET", url, headers=headers, data=payload)
#
#     status_code = response.status_code
#     result = response.text
#     #=============================
#
#     return amount, status_code, result



file_path = '../data/operations.json'                   # путь до json файла
transactions = read_financial_transactions(file_path)

# print(transactions)

#print(proverka(transactions))




tor = "RUB"
valute_from = "USD"
amounts = "8221.37"

ref = convert(tor, valute_from, amounts)
print(set(ref)['result'])

"""
{
    "success": true,
    "query": {
        "from": "USD",
        "to": "RUB",
        "amount": 8221.37
    },
    "info": {
        "timestamp": 1720689976,
        "rate": 87.950001
    },
    "date": "2024-07-11",
    "result": 723069.499721
}
"""








"""
2. Реализуйте функцию, которая принимает на вход транзакцию и возвращает сумму транзакции (amount) в рублях,
тип данных — float.

Если транзакция была в USD или EUR, происходит обращение к внешнему API для получения
текущего курса валют и конвертации суммы операции в рубли.
Для конвертации валюты воспользуйтесь Exchange Rates Data API: https://apilayer.com/exchangerates_data-api.

Функцию конвертации поместите в модуль external_api.


Используйте переменные окружения из файла .env для сокрытия чувствительных данных (токенов доступа для API).
Создайте шаблон файла .env и разместите в репозитории на GitHub.

Напишите тесты для новых функций, используйте Mock и patch.
"""
