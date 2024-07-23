from src.utils import read_financial_transactions
from src.financial import reader_file_transaction_csv, reader_file_transaction_excel
from src.search_transaction import search_transactions, count_transaction_categories
from src.processing import filter_by_state, sort_by_date


# ================================================= 1 =============================================================


def selections_file(u_input):
    """Выбор формата файла транзакций"""
    json_path = "../data/operations.json"
    csv_path = "../data/transactions.csv"
    xlsx_path = "../data/transactions_excel.xlsx"

    transactions = []

    if u_input == 1:
        print("Для обработки выбран JSON-файл\n")
        transactions = read_financial_transactions(json_path)
    elif u_input == 2:
        print("Для обработки выбран CSV-файл\n")
        transactions = reader_file_transaction_csv(csv_path)
    elif u_input == 3:
        print("Для обработки выбран XLSX-файл\n")
        transactions = reader_file_transaction_excel(xlsx_path)
    else:
        print(f"Такой вариант не найден, попробуйте ещё раз.")

    return transactions


# ================================================= 2 =============================================================


def status_operations(transactions, answer):
    """Выбор статуса операции"""
    status = ["EXECUTED", "CANCELED", "PENDING"]

    while True:
        if answer in status:
            print(f'Операции отфильтрованы по статусу "{answer}"')
            result = filter_by_state(transactions, answer)
            break
        else:
            print(f'Статус операции "{answer}" недоступен.\n')
            print(f"Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING")
            answer = str(input(f"Выберете интересующие Вас операции:"
                               f"Пользователь: ").upper())

    return result


# ================================================= 3 =============================================================


def user_choise_data(transactions):
    answer_1 = input(f"Программа: Отсортировать операции по дате? Да/Нет\n")

    if answer_1 == "да":
        answer_2 = int(input(f"1. По убыванию\n2. Возрастанию\n"))
        while True:
            if answer_2 == 1:
                result = sort_by_date(transactions, True)
                break
            elif answer_2 == 2:
                result = sort_by_date(transactions, False)
                break
            else:
                print(f'Статус операции "{answer_2}" недоступен.\n')
                print(f"Вы ввели некорректный вариант, попробуйте еще.")
                answer_2 = int(input(f"1. По убыванию\n2. Возрастанию\n"))
        return result
    else:
        return transactions


if __name__ == "__main__":
    # ================================================= 1 =============================================================
    user_input_1 = int(input(f"Привет! Добро пожаловать в программу работы с банковскими транзакциями.\n"
                             f"Выберите необходимый пункт меню:\n"
                             f"1. Получить информацию о транзакциях из JSON-файла\n"
                             f"2. Получить информацию о транзакциях из CSV-файла\n"
                             f"3. Получить информацию о транзакциях из XLSX-файла\n"
                             f"Пользователь:  "))

    format_file = selections_file(user_input_1)
    # print(selections_file(user_input_1))

    # ================================================= 2 =============================================================
    user_input_2 = str(input(f"Выберете интересующие Вас операции: "
                             f"Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING\n"
                             f"Пользователь: ").upper())

    user_status_operation = status_operations(format_file, user_input_2)
    # print(user_status_operation)

    """ 
    После пользователь выбирает статус интересующих его операций.
    Не забудьте, что для пользователя executed, Executed и EXECUTED — это одно и то же, 
    а для программы — разное. Используйте приведение к единому регистру.

    Программа: Введите статус, по которому необходимо выполнить фильтрацию. 
    Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING

    Пользователь: EXECUTED
    Программа: Операции отфильтрованы по статусу "EXECUTED"

    =============
    В случае, если пользователь ввел неверный статус, программа не должна падать в ошибку,            
    а должна возвращать пользователя к вводу корректного статуса:

    Пользователь: test

    Программа: Статус операции "test" недоступен.

    Программа: Введите статус, по которому необходимо выполнить фильтрацию. 
    Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING

    """

    # ================================================= 3 =============================================================


""" После фильтрации программа выводит следующие вопросы для уточнения выборки операций, 
необходимых пользователю, и выводит в консоль операции, соответствующие выборке пользователя:
Программа: Отсортировать операции по дате? Да/Нет
Пользователь: да"""

    res = user_choise_data(user_status_operation)
    print(res)


"""
Программа: Отсортировать по возрастанию или по убыванию? 

Пользователь: по возрастанию/по убыванию

Программа: Выводить только рублевые транзакции? Да/Нет

Пользователь: да

Программа: Отфильтровать список транзакций по определенному слову 
в описании? Да/Нет

Пользователь: да/нет

Программа: Распечатываю итоговый список транзакций...

Программа: 
Всего банковских операций в выборке: 4

08.12.2019 Открытие вклада 
Счет **4321
Сумма: 40542 руб. 

12.11.2019 Перевод с карты на карту
MasterCard 7771 27** **** 3727 -> Visa Platinum 1293 38** **** 9203
Сумма: 130 USD

18.07.2018 Перевод организации 
Visa Platinum 7492 65** **** 7202 -> Счет **0034
Сумма: 8390 руб.

03.06.2018 Перевод со счета на счет
Счет **2935 -> Счет **4321
Сумма: 8200 EUR

Если выборка оказалась пустой, программа выводит сообщение:

Программа: Не найдено ни одной транзакции, подходящей под ваши
условия фильтрации
"""
