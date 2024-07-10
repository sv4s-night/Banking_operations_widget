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

import requests


def convert():
    """Функция конвертации по API"""
    valute_from = "USD"
    valute_to = "RUS"
    amount = 10

    # url = "https://api.apilayer.com/exchangerates_data/convert?to={to}&from={from}&amount={amount}"
    url = f"https://api.apilayer.com/exchangerates_data/convert?to={valute_to}&from={valute_from}&amount={amount}"

    payload = {}
    headers = {
        "apikey": "sctfncfS2MC1onu8cMTgSxeEqFY0FZBy"
    }
    response = requests.request("GET", url, headers=headers, data=payload)

    status_code = response.status_code
    result = response.text
    return result



print(convert())






"""

import requests

url = "https://api.apilayer.com/exchangerates_data/convert?to={to}&from={from}&amount={amount}"

payload = {}
headers= {
  "apikey": "sctfncfS2MC1onu8cMTgSxeEqFY0FZBy"
}

response = requests.request("GET", url, headers=headers, data = payload)

status_code = response.status_code
result = response.text


** Слово, заключенное в фигурные скобки "{ }" в коде, означает, что это параметр, и его следует заменить собственными значениями при выполнении (также перезаписывая фигурные скобки).


===================================================
Ниже приведен пример ответа от конечной точки.

{
  "date": "2018-02-22",
  "historical": "",
  "info": {
    "rate": 148.972231,
    "timestamp": 1519328414
  },
  "query": {
    "amount": 25,
    "from": "GBP",
    "to": "JPY"
  },
  "result": 3724.305775,
  "success": true
}

"""