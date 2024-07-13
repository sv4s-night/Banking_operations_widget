import json

import src.external_api


def read_financial_transactions(path: str) -> list[dict:dict]:
    """Функция принимает путь до json файла и возвращает список словарей с данными о финансовых транзакциях"""
    try:
        with open(path, "r", encoding="UTF-8") as file:
            data = json.load(file)
            if isinstance(data, list):
                return data
            else:
                return []
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def checking_currency(transaction: list, required_currency: str) -> float:
    """Функция проверки. Является валюта транзакции искомой(required_currency), если нет, то конвертируется"""
    my_dict = {
        "desired_currency": required_currency,
        "currency_from": transaction[0]["operationAmount"]["currency"]["code"],
        "amount": transaction[0]["operationAmount"]["amount"],
    }

    if my_dict["currency_from"] != required_currency:
        exchange_rate = src.external_api.currency_conversion(my_dict)
        return exchange_rate
    else:
        return my_dict["amount"]
