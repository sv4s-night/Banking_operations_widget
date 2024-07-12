import json
import os

import requests
from dotenv import load_dotenv

load_dotenv("../.env")


def currency_conversion(required_currency: str, currency_from: str, amount: str) -> float:
    """Обращение к API Apilayer.com для конвертации валюты"""
    url = (
        f"https://api.apilayer.com/exchangerates_data/convert"
        f"?to={required_currency}&from={currency_from}&amount={amount}"
    )
    payload = {}

    # API_KEY - для ознакомления, перейти в .env.example
    headers = {"apikey": f"{os.getenv("API_KEY")}"}

    response = requests.request("GET", url, headers=headers, data=payload)
    # status_code = response.status_code
    result = json.loads(response.text)
    return result
