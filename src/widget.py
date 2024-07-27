import re
from collections import Counter

from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(mask_info_card: str) -> str:
    """Функция маскировки карты и счета"""

    masquerade = mask_info_card.split(" ")

    for account_or_card in masquerade:
        if account_or_card.isdigit():

            if len(account_or_card) == 16:
                result = " ".join(masquerade[0:-1]) + get_mask_card_number(account_or_card)
            elif len(account_or_card) > 16:
                result = " ".join(masquerade[0:-1]) + get_mask_account(account_or_card)
            else:
                result = "Вы допустили ошибку при вводе данных счета или карты"

    return result


def get_date(date_str: str) -> str:
    """Функция преобразования даты"""

    parts = date_str.split("T")[0].split("-")
    return f"{parts[2]}.{parts[1]}.{parts[0]}"


def search_transactions(transactions, search_string):
    """Поиск по описанию в транзакции, по заданному слову"""
    return [
        transaction
        for transaction in transactions
        if re.search(search_string, transaction["description"], flags=re.IGNORECASE)
    ]


def count_transaction_categories(transactions):
    """Функция подсчета количества операций по категориям"""
    categories = [transaction["description"] for transaction in transactions]
    category_counts = Counter(categories)
    return category_counts
