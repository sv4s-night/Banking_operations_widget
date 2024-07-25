import re


def search_transactions(transactions, search_string):
    """Поиск по описанию транзакции"""
    return [transaction for transaction in transactions if
            re.search(search_string, transaction['description'], flags=re.IGNORECASE)]




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
#
#
# transactions = [{
#     "id": 142264268,
#     "state": "EXECUTED",
#     "date": "2019-04-04T23:20:05.206878",
#     "operationAmount": {
#         "amount": "79114.93",
#         "currency": {
#             "name": "USD",
#             "code": "USD"
#         }
#     },
#     "description": "Transfer from account to account",
#     "from": "Account 19708645243227258542",
#     "to": "Account 75651667383060284188"
# }]
#
# categories = ["Transfer from account to account", "Payment", "Withdrawal"]
#
# result = count_transaction_categories(transactions, categories)
# print(result)


# =================================================================================================================
#

#
# print("Распечатываю итоговый список транзакций...\n")
# print(f"Всего банковских операций в выборке: {len(result)}")
#
# if result is []:
#     return "Не найдено ни одной транзакции, подходящей под ваши условия фильтрации"
# else:
#     for i in result:
#         data = get_data(i["date"])
#         description = i["description"]
#         from_ = get_mask_card_number(i.get("from", ""))
#         to_ = get_mask_card_number(i.get("to", ""))
#         amount = i["operationAmount"]["amount"]
#         name = i["operationAmount"]["currency"]["name"]
#
#         print(f"{data} {description}\n{from_} -> {to_}\nСумма: {amount} {name}\n")
# return "finish"
