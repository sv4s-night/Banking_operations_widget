def filter_by_state(data_array, state='EXECUTED'):
    """Функция фильтрации в операциях по счетам (исполнено и отказано)"""

    return [d for d in data_array if d.get('state') == state]


def sort_by_data(data_array, reverse=False):
    """Функция сортировки по дате"""

    return sorted(data_array, key=lambda x: x['date'], reverse=reverse)
