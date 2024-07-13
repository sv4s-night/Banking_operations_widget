import json
import os

import requests
from dotenv import load_dotenv

load_dotenv("../.env")


def currency_conversion(data: dict) -> float:
    """Обращение к API Apilayer.com для конвертации валюты"""
    url = (
        f"https://api.apilayer.com/exchangerates_data/convert"
        f"?to={data["desired_currency"]}&from={data["currency_from"]}&amount={data["amount"]}"
    )
    payload = {}

    # API_KEY - для ознакомления, перейти в .env.example
    headers = {"apikey": f"{os.getenv("API_KEY")}"}

    response = requests.request("GET", url, headers=headers, data=payload)
    # status_code = response.status_code
    result = json.loads(response.text)
    return result
