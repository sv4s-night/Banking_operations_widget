import json
import logging

utils_logger = logging.getLogger("utils")
utils_logger.setLevel(logging.INFO)
file_handler = logging.FileHandler("../logs/utils.log")
file_formatter = logging.Formatter("%(asctime)s - %(filename)s - %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
utils_logger.addHandler(file_handler)


def read_financial_transactions(path: str) -> list[dict:dict]:
    """Функция принимает путь до json файла и возвращает список словарей с данными о финансовых транзакциях"""
    try:
        with open(path, "r", encoding="UTF-8") as file:
            data = json.load(file)
            if isinstance(data, list):
                utils_logger.info("get_mask_card_number: The list has been created")
                return data
            else:
                utils_logger.info("get_mask_card_number: an empty list has been generated")
                return []
    except (FileNotFoundError, json.JSONDecodeError):
        utils_logger.warning("get_mask_card_number FileNotFoundError")
        return []
