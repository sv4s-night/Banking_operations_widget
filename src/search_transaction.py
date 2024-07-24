""" """
import re
""" 1 Задача
Напишите функцию, которая будет принимать список словарей с данными о банковских операциях и строку поиска, 
а возвращать список словарей, у которых в описании есть данная строка. 
"""

def search_transactions(data, search_string):
    """Поиск по описанию транзакции"""
    return [transaction for transaction in data if re.search(search_string, transaction['description'])]

    # pattern = rf"{search_string}"
    # result_transactions_dict = [
    #     transaction
    #     for transaction in transactions
    #     if re.findall(pattern, transaction["description"], flags=re.IGNORECASE)
    # ]
    # return result_transactions_dict




#
# def sorting_transactions_by_description(transactions: List[Dict], search_string: str) -> List[Dict]:
#     """Функция принимает список транзакций (словарей) и слово для сортировки.
#     Возвращает список транзакций (словарей), у которых в описании есть указанное слово."""
#     pattern = rf"{search_string}"
#     result_transactions_dict = [
#         transaction
#         for transaction in transactions
#         if re.findall(pattern, transaction["description"], flags=re.IGNORECASE)
#     ]
#     return result_transactions_dict







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


# =================================================================================================================

next_choice_word = """\nОтфильтровать список транзакций по определенному слову в описании? Да/Нет"""
input_user_word = input(f"{next_choice_word}\n").lower()
while input_user_word not in ["да", "нет"]:
    print("\nВвели некорректную фильтрацию\nПопробуйте еще раз:")
    input_user_word = input(f"{next_choice_word}\n").lower()
else:
    if input_user_word == "да":
        word_filter = input("Введите слово для поиска:\n")

        if input_user_rub == "да":
            list_result = [r for r in [*result]]
            result = search_transactions([*result], word_filter)

        else:
            result = search_transactions(result, word_filter)

print("Распечатываю итоговый список транзакций...\n")
print(f"Всего банковских операций в выборке: {len(result)}")

if result is []:
    return "Не найдено ни одной транзакции, подходящей под ваши условия фильтрации"
else:
    for i in result:
        data = get_data(i["date"])
        description = i["description"]
        from_ = get_mask_card_number(i.get("from", ""))
        to_ = get_mask_card_number(i.get("to", ""))
        amount = i["operationAmount"]["amount"]
        name = i["operationAmount"]["currency"]["name"]

        print(f"{data} {description}\n{from_} -> {to_}\nСумма: {amount} {name}\n")
return "finish"