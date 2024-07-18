from src.generators import card_number_generator, filter_by_currency, transaction_descriptions
from src.decorators import log
from src.external_api import checking_currency
from src.masks import get_mask_account, get_mask_card_number
from src.utils import read_financial_transactions

import pandas as pd

from src.financial import reading_file_csv_or_xlsx



if __name__ == "__main__":
    # ================================================ lesson 9.1 ===
    # number_card = get_mask_card_number("1111222233334444")
    # print(f"Функция маскировки номера карты: " + number_card)
    #
    # mask_account = get_mask_account("4444555566667777")
    # print(f"Функция маскировки номера счета: " + mask_account)

    # ================================================ lesson 12.1 ===
    # file_path = "../data/operations.json"
    # transactions = read_financial_transactions(file_path)
    # # print(transactions)
    # result = checking_currency(transactions)
    # # print(result)
    # print(round(result["result"], 2))

    # ================================================ lesson 13.1 ===

    csv_file = "../data/transactions.csv"
    xlsx_file = "../data/transactions_excel.xlsx"

    df = reading_file_csv_or_xlsx(xlsx_file)

    print(f"Количество строк, столбцов: {df.shape}\n")  # — выводит размер таблицы;
    print(f"Пример содержимого файла:\n {df.head()}")   # — выводит первые несколько строк таблицы;
    print(f"Статистическая информация:\n {df.describe()}")  # — выводит основную статистическую информацию по таблице;
    print(f"Уникальные значения в столбце:\n{df.value_counts()}")  # — выводит количество уникальных значений в столбце;
