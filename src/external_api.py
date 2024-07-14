import json
import os

import requests
from dotenv import load_dotenv

load_dotenv("../.env")


def checking_currency(transaction: list) -> float:
    """Функция проверки. Является валюта транзакции искомой(required_currency), если нет, то конвертируется"""
    checked_data = {
        "required_currency": "RUB",
        "currency_from": transaction[0]["operationAmount"]["currency"]["code"],
        "amount": transaction[0]["operationAmount"]["amount"],
    }

    if checked_data["currency_from"] != checked_data["required_currency"]:

        url = (
            f"https://api.apilayer.com/exchangerates_data/convert"
            f"?to={checked_data["required_currency"]}&from={checked_data["currency_from"]}"
            f"&amount={checked_data["amount"]}"
        )
        payload = {}

        # API_KEY - для ознакомления, перейти в .env.example
        headers = {"apikey": f"{os.getenv("API_KEY")}"}

        response = requests.request("GET", url, headers=headers, data=payload)
        # status_code = response.status_code
        result = json.loads(response.text)
        return result
    else:
        return checked_data["amount"]
