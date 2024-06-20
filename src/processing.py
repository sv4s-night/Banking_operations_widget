from typing import Any


def filter_by_state(data_array: Any[str], state: str = "EXECUTED") -> Any[str]:
    """Функция фильтрации в операциях по счетам (исполнено и отказано)"""

    return [d for d in data_array if d.get("state") == state]


def sort_by_data(data_array: Any[str], reverse: bool = False) -> Any[str]:
    """Функция сортировки по дате"""

    return sorted(data_array, key=lambda x: x["date"], reverse=reverse)
