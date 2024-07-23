""" """
import re
""" 1 Задача
Напишите функцию, которая будет принимать список словарей с данными о банковских операциях и строку поиска, 
а возвращать список словарей, у которых в описании есть данная строка. 

При реализации этой функции можно использовать библиотеку re для работы с регулярными выражениями.
Расположение новой функции в структуре проекта определите самостоятельно.
"""


def search_transactions(data, search_string):
    return [transaction for transaction in data if re.search(search_string, transaction['description'])]




""" 2 Задача
Напишите функцию, которая будет принимать список словарей с данными о банковских операциях и список категорий операций, 
а возвращать словарь, в котором ключи — это названия категорий, а значения — это количество операций в каждой категории.
Категории операций хранятся в поле description.

Расположение новой функции в структуре проекта определите самостоятельно.
"""


def count_transaction_categories(transactions, categories):
    category_count = {category: 0 for category in categories}
    for transaction in transactions:
        description = transaction.get("description", "")
        if description in category_count:
            category_count[description] += 1
    return category_count


transactions = [{
    "id": 142264268,
    "state": "EXECUTED",
    "date": "2019-04-04T23:20:05.206878",
    "operationAmount": {
        "amount": "79114.93",
        "currency": {
            "name": "USD",
            "code": "USD"
        }
    },
    "description": "Transfer from account to account",
    "from": "Account 19708645243227258542",
    "to": "Account 75651667383060284188"
}]

categories = ["Transfer from account to account", "Payment", "Withdrawal"]

result = count_transaction_categories(transactions, categories)
print(result)
