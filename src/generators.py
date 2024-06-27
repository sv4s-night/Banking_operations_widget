def filter_by_currency(transact, currency):
    """Функция возвращающая поочередно операции в которых указана заданная валюта"""
    for transaction in transact:
        if transaction["operationAmount"]["currency"]["code"] == currency:
            yield transaction


def transaction_descriptions(transactions):
    """Функция возвращающая описание каждой операции по очереди"""
    for transaction in transactions:
        yield transaction.get("description", "No description available")


def card_number_generator(start, end):
    """Функция генерирующая номера карт в заданном диапазоне"""
    for i in range(start, end + 1):
        yield ('{:04d} {:04d} {:04d} {:04d}'
               .format(i // 10 ** 12 % 10 ** 4, i // 10 ** 8 % 10 ** 4, i // 10 ** 4 % 10 ** 4, i % 10 ** 4))
