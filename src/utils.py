import json


def read_financial_transactions(path: str) -> list[dict:dict]:
    """Функция принимает путь до json файла и возвращает список словарей с данными о финансовых транзакциях"""
    try:
        with open(path, "r", encoding="UTF-8") as file:
            data = json.load(file)
            if isinstance(data, list):
                return data
            else:
                return []
    except (FileNotFoundError, json.JSONDecodeError):
        return []
