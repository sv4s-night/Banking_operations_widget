"""
Используйте переменные окружения из файла .env для сокрытия чувствительных данных (токенов доступа для API).
Создайте шаблон файла .env и разместите в репозитории на GitHub.

Напишите тесты для новых функций, используйте Mock и patch.
"""
import json
import os
import requests
from dotenv import load_dotenv

load_dotenv('../.env')


def currency_conversion(to, val_from, amount) -> float:
    """Обращение к API Apilayer.com для конвертации валюты"""
    url = f"https://api.apilayer.com/exchangerates_data/convert?to={to}&from={val_from}&amount={amount}"
    payload = {}

    # API_KEY - для ознакомления, перейти в .env.example
    headers = {
        "apikey": f"{os.getenv("API_KEY")}"
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    # status_code = response.status_code
    result = json.loads(response.text)
    return round(result["result"], 2)
