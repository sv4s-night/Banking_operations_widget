# from src.generators import card_number_generator, filter_by_currency, transaction_descriptions
# from src.decorators import log
from src.external_api import checking_currency
from src.utils import read_financial_transactions
from src.masks import get_mask_account, get_mask_card_number
import logging


masks_logger = logging.getLogger("masks")
masks_logger.setLevel(logging.INFO)
file_handler = logging.FileHandler("../logs/masks.log")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
masks_logger.addHandler(file_handler)


if __name__ == "__main__":

    # ================================================ lesson 9.1
    number_card = get_mask_card_number("1111222233334444")
    print(f"Функция маскировки номера карты: " + number_card)

    mask_account = get_mask_account("4444555566667777")
    print(f"Функция маскировки номера счета: " + mask_account)


    # ================================================ lesson 12.1
    file_path = "../data/operations.json"
    transactions = read_financial_transactions(file_path)
    # print(transactions)
    result = checking_currency(transactions)
    # print(result)
    print(round(result["result"], 2))



"""
1. Задачи
Создайте логеры для перечисленных модулей: masks,utils.

2. Задачи
Реализуйте запись логов в файл. Логи должны записываться в папку logs в корне проекта. 
Файлы логов должны иметь расширение .log.

3. Задачи
Формат записи лога в файл должен включать метку времени, название модуля, уровень серьезности и сообщение, 
описывающее событие или ошибку, которые произошли.

4. Задачи
Лог должен перезаписываться при каждом запуске приложения.   
"""