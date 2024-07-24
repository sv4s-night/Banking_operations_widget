from src.utils import read_financial_transactions
from src.financial import reader_file_transaction_csv, reader_file_transaction_excel
#from src.search_transaction import search_transactions, count_transaction_categories
from src.processing import filter_by_state, sort_by_date
from external_api import checking_currency
from generators import filter_by_currency


# ================================================= 1 =============================================================


def selections_file():
    """Выбор формата файла транзакций"""

    user_input = int(input(f"Привет! Добро пожаловать в программу работы с банковскими транзакциями.\n"
                             f"Выберите необходимый пункт меню:\n"
                             f"1. Получить информацию о транзакциях из JSON-файла\n"
                             f"2. Получить информацию о транзакциях из CSV-файла\n"
                             f"3. Получить информацию о транзакциях из XLSX-файла\n"
                             f"Пользователь:  "))

    json_path = "../data/operations.json"
    csv_path = "../data/transactions.csv"
    xlsx_path = "../data/transactions_excel.xlsx"

    transactions = []

    if user_input == 1:
        print("Для обработки выбран JSON-файл\n")
        transactions = read_financial_transactions(json_path)
    elif user_input == 2:
        print("Для обработки выбран CSV-файл\n")
        transactions = reader_file_transaction_csv(csv_path)
    elif user_input == 3:
        print("Для обработки выбран XLSX-файл\n")
        transactions = reader_file_transaction_excel(xlsx_path)
    else:
        print(f"Такой вариант не найден, попробуйте ещё раз.")

    return transactions
# ================================================= 2 =============================================================


def status_operations(transactions):
    """Выбор статуса операции"""
    user_input = str(input(f"Выберете интересующие Вас операции: "
                             f"Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING\n"
                             f"Пользователь: ").upper())


    status = ["EXECUTED", "CANCELED", "PENDING"]

    while True:
        if user_input in status:
            print(f'Операции отфильтрованы по статусу "{user_input}"')
            result = filter_by_state(transactions, user_input)
            break
        else:
            print(f'Статус операции "{user_input}" недоступен.\n')
            print(f"Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING")
            answer = str(input(f"Выберете интересующие Вас операции:"
                               f"Пользователь: ").upper())

    return result
# ================================================= 3 =============================================================


def sorting_by_date(transactions):
    """Сортировка по дате, по возрастанию и убыванию"""
    answer_1 = input(f"Программа: Отсортировать операции по дате? Yes/No\nПользователь: ").lower()

    while answer_1 not in ["yes", "no"]:
        print(f'\nСтатус операции "{answer_1}" недоступен.')
        print(f"Был введен некорректный вариант, попробуйте еще раз.")
        answer_1 = input(f"Программа: Отсортировать операции по дате? Yes/No\nПользователь: ").lower()

    else:
        if answer_1 == "yes":
            answer_2 = input(f"1. По убыванию\n2. Возрастанию\nПользователь: ")
            while answer_2 not in ["1", "2"]:
                print(f'\nСтатус операции "{answer_2}" недоступен.')
                print(f"Был введен некорректный вариант, попробуйте еще раз.")
                answer_2 = input(f"1. По возрастанию\n2. По убыванию\nПользователь: ")

            else:
                if answer_2 == "1":
                    result = sort_by_date(transactions, True)
                    return result
                elif answer_2 == "2":
                    result = sort_by_date(transactions, False)
                    return result

        elif answer_1 == "no":
            return transactions
# ================================================= 4 =============================================================


def amount_by_rub(transactions):
    """Вывод рублевых транзакций"""
    while True:
        answer_1 = input("Выводить только рублевые транзакции? Yes/No\nПользователь: ").lower()

        if answer_1 == "yes":
            new_list_sort = []
            for item in transactions:
                if item["operationAmount"]["currency"]["code"] == "RUB":
                    new_list_sort.append(item)

            return new_list_sort
        elif answer_1 == "no":
            return transactions
        else:
            print(f'\nСтатус операции "{answer_1}" недоступен.')
            print(f"Был введен некорректный вариант, попробуйте еще раз.")
# ================================================= 5 =============================================================


"""
Программа: Отфильтровать список транзакций по определенному слову в описании? Да/Нет
"""

# def search_by_word(transactions):
#     """Поиск по слову в транзакции"""
#     while True:
#         answer_1 = input(f"Отфильтровать список транзакций по определенному слову в описании? Yes/No\nПользователь: ").lower()
#
#         if answer_1 == "yes":
#             word_search = input("Введите искомое слово:\nПользователь: ")
#             result = search_transactions(transactions, word_search)
#             return result
#
#         elif answer_1 == "no":
#             return transactions
#         else:
#             print(f'\nСтатус операции "{answer_1}" недоступен.')
#             print(f"Был введен некорректный вариант, попробуйте еще раз.")






    # answer_1 = input(f"Отфильтровать список транзакций по определенному слову в описании? Yes/No\nПользователь: ").lower()
    #
    # while answer_1 not in ["yes", "no"]:
    #     print(f"Был введен некорректный вариант, попробуйте еще раз.")
    #     answer_1 = input(f"Отфильтровать список транзакций по определенному слову в описании? Yes/No\nПользователь: ").lower()
    # else:
    #     if answer_1 == "yes":
    #         word_search = input("Введите искомое слово:\nПользователь: ")
    #         result = search_transactions(transactions, word_search)
    #         return result
    #
    #     elif answer_1 == "no":
    #         return transactions



















if __name__ == "__main__":
    # ================================================= 1 =============================================================
    # выбор формата файла
    format_file = selections_file()
    # print(selections_file(user_input_1))

    # ================================================= 2 =============================================================
    # выбор операции
    user_status_operation = status_operations(format_file)
    # print(user_status_operation)

    # ================================================= 3 =============================================================
    # фильтрация по дате и сортировка по убыванию и возрастанию
    first_stage = sorting_by_date(user_status_operation)
    #print(first_stage)

    # ================================================= 3 =============================================================
    # Вывод только рублевых транзакции
    second_stage = amount_by_rub(first_stage)
    print(second_stage)

    # ================================================= 4 =============================================================
    # Фильтрация списка транзакций по определенному слову в описании
    #third_stage = search_by_word(second_stage)
    #print(third_stage)




    # ================================================= not working =============================================================
    # counter
    # get_mask_card_number, get_mask_account      src.masks





    """
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
