from src.widget import mask_account_card, get_data
from src.processing import filter_by_state, sort_by_date

if __name__ == "__main__":
    # Проверочные данные урока 9.2

    user_info = str(input("Введите данные Вашей карты или счета:\n"))
    print(mask_account_card(user_info))

    operation_date = str(input("Введите дату операции:\n"))
    print(get_data(operation_date))

    data_list = [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]

    filtered_data = filter_by_state(data_list, state="CANCELED")
    print(f"Сортировка по статусу операции:\n{filtered_data}")

    sorted_date = sort_by_date(data_list, ascending=False)
    print(f"Сортировка по дате:\n{sorted_date}")
