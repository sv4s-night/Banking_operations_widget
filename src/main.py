# from src.widget import mask_account_card, get_data
from src.processing import filter_by_state, sort_by_data

if __name__ == "__main__":
    # Проверочные данные урока 9.2

    # get_user_info = str(input("Введите данные Вашей карты или счета:\n"))
    # print(mask_account_card(get_user_info))

    # info_data = str(input("Введите дату операции:\n"))
    # print(get_data(info_data))

    dict_list = [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]

    sorted_dicts = filter_by_state(dict_list, state="CANCELED")
    print(f"Сортировка по статусу операции:\n{sorted_dicts}")

    sorted_data = sort_by_data(dict_list, reverse=True)
    print(f"Сортировка по дате:\n{sorted_data}")
