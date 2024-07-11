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
    result = json.loads(response.text)
    return round(result["result"], 2)


def proverka(transaction):
    """Функция проверки явл ли Рублем"""
    tor = "RUB"
    valute_from = transaction[0]["operationAmount"]["currency"]["code"]
    amount = transaction[0]["operationAmount"]["amount"]

    if valute_from != "RUB":
        # API
        exchange_rate = convert(tor, valute_from, amount)
        # amount_rubles = transactions["amount"] * exchange_rate
        return exchange_rate
    else:
        return amount







file_path = '../data/operations.json'                   # путь до json файла
transactions = read_financial_transactions(file_path)

# print(transactions)



print(proverka(transactions))



# проверка def convert()
# tor = "RUB"
# valute_from = "USD"
# amounts = "8221.37"
# print(convert(tor, valute_from, amounts))  # 723069.771027 результат


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
