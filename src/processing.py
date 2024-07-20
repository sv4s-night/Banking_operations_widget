# ================================================ HW lesson 10.1 ===
from typing import Any, Dict, List


def filter_by_state(data_array: List[Dict[str, Any]], state: str = "EXECUTED") -> List[Dict[str, Any]]:
    """Функция фильтрации в операциях по счетам (исполнено и отказано)"""

    return [d for d in data_array if d.get("state") == state]


def sort_by_date(data_array: List[Dict[str, Any]], ascending: bool = True) -> List[Dict[str, Any]]:
    """Функция сортировки по дате"""

    return sorted(data_array, key=lambda x: x["date"], reverse=ascending)
