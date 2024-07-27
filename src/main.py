from src.financial import reader_file_transaction_csv, reader_file_transaction_excel
from src.processing import filter_by_state, sort_by_date
from src.utils import read_financial_transactions
from widget import count_transaction_categories, get_date, mask_account_card, search_transactions


def selections_file():
    """Выбор формата файла транзакций"""

    user_input = int(
        input(
            "Программа: Привет! Добро пожаловать в программу работы с банковскими транзакциями.\n"
            "Программа: Выберите необходимый пункт меню:\n"
            "Программа: 1. Получить информацию о транзакциях из JSON-файла\n"
            "Программа: 2. Получить информацию о транзакциях из CSV-файла\n"
            "Программа: 3. Получить информацию о транзакциях из XLSX-файла\n"
            "Пользователь:  "
        )
    )

    json_path = "../data/operations.json"
    csv_path = "../data/transactions.csv"
    xlsx_path = "../data/transactions_excel.xlsx"

    transactions = []

    if user_input == 1:
        print("Программа: Для обработки выбран JSON-файл\n")
        transactions = read_financial_transactions(json_path)
    elif user_input == 2:
        print("Программа: Для обработки выбран CSV-файл\n")
        transactions = reader_file_transaction_csv(csv_path)
    elif user_input == 3:
        print("Программа: Для обработки выбран XLSX-файл\n")
        transactions = reader_file_transaction_excel(xlsx_path)
    else:
        print("Программа: Такой вариант не найден, попробуйте ещё раз.")

    return transactions


def status_operations(transactions):
    """Выбор статуса операции"""
    user_input = str(
        input(
            "Программа: Выберете интересующие Вас операции: "
            "Программа: Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING\n"
            "Пользователь: "
        ).upper()
    )

    status = ["EXECUTED", "CANCELED", "PENDING"]

    while True:
        if user_input in status:
            print(f'Программа: Операции отфильтрованы по статусу "{user_input}"\n')
            result = filter_by_state(transactions, user_input)
            break
        else:
            print(f'Программа: Статус операции "{user_input}" не найден.\n')
            print("Программа: Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING")
            user_input = str(input("Программа: Выберете интересующие Вас операции:\nПользователь: ").upper())

    return result


def sorting_by_date(transactions):
    """Сортировка по дате, по возрастанию и убыванию"""
    answer_1 = input("Программа: Отсортировать операции по дате? Yes/No\nПользователь: ").lower()

    while answer_1 not in ["yes", "no"]:
        print(f'\nПрограмма: Статус операции "{answer_1}" недоступен.')
        print("\nПрограмма: Был введен некорректный вариант, попробуйте еще раз.")
        answer_1 = input("Программа: Отсортировать операции по дате? Yes/No\nПользователь: ").lower()

    else:
        if answer_1 == "yes":
            answer_2 = input("\nПрограмма: 1. По убыванию\nПрограмма: 2. По возрастанию\nПользователь: ")
            while answer_2 not in ["1", "2"]:
                print(f'\nПрограмма: Статус операции "{answer_2}" недоступен.')
                print("Программа: Был введен некорректный вариант, попробуйте еще раз.")
                answer_2 = input("Программа: 1. По убыванию\nПрограмма: 2. По возрастанию\nПользователь: ")

            else:
                if answer_2 == "1":
                    result = sort_by_date(transactions, True)
                    return result
                elif answer_2 == "2":
                    result = sort_by_date(transactions, False)
                    return result

        elif answer_1 == "no":
            return transactions


def amount_by_rub(transactions):
    """Вывод рублевых транзакций"""
    while True:
        answer_1 = input("\nПрограмма: Выводить только рублевые транзакции? Yes/No\nПользователь: ").lower()

        if answer_1 == "yes":
            new_list_sort = []
            for item in transactions:
                if item["operationAmount"]["currency"]["code"] == "RUB":
                    new_list_sort.append(item)

            return new_list_sort
        elif answer_1 == "no":
            return transactions
        else:
            print(f'\nПрограмма: Статус операции "{answer_1}" недоступен.')
            print("Программа: Был введен некорректный вариант, попробуйте еще раз.")


def search_by_word(transactions):
    """Отфильтровать список транзакций по определенному слову в описании"""
    while True:
        answer_1 = input(
            "\nПрограмма: Отфильтровать список транзакций по определенному слову " "в описании? Yes/No\nПользователь: "
        ).lower()

        if answer_1 == "yes":
            word_search = input("\nПрограмма: Введите искомое слово:\nПользователь: ")
            result = search_transactions(transactions, word_search)
            return result

        elif answer_1 == "no":
            return transactions
        else:
            print(f'\nПрограмма: Статус операции "{answer_1}" недоступен.')
            print("Программа: Был введен некорректный вариант, попробуйте еще раз.")


def conclusion_results(transactions):
    """Вывод итогового сообщения"""
    print("\nПрограмма: Распечатываю итоговый список транзакций...")
    print(f"Программа: Всего банковских операций в выборке: {len(transactions)}\n")
    print(f"Программа: {count_transaction_categories(transactions)}\n")

    if transactions is []:
        return "Программа: Не найдено ни одной транзакции, подходящей под ваши условия фильтрации"
    else:
        for item in transactions:
            date = get_date(item["date"])
            description = item["description"]
            amount = item["operationAmount"]["amount"]
            name = item["operationAmount"]["currency"]["name"]

            if "Перевод" in description:
                from_ = mask_account_card(item.get("from", ""))
                to_ = mask_account_card(item.get("to", ""))
                print(f"{date} {description}\n{from_} -> {to_}\nСумма: {amount} {name}\n")
            elif "Открытие" in description:
                to_ = mask_account_card(item.get("to", ""))
                print(f"{date} {description}\n{to_}\nСумма: {amount} {name}\n")

    return "Программа: Конец выполнения операции"


if __name__ == "__main__":
    # выбор формата файла
    format_file = selections_file()
    # print(selections_file(user_input_1))

    # выбор операции
    user_status_operation = status_operations(format_file)
    # print(user_status_operation)

    # фильтрация по дате и сортировка по убыванию и возрастанию
    first_stage = sorting_by_date(user_status_operation)
    # print(first_stage)

    # Вывод только рублевых транзакции
    second_stage = amount_by_rub(first_stage)
    # print(second_stage)

    # Фильтрация списка транзакций по определенному слову в описании
    third_stage = search_by_word(second_stage)
    # print(third_stage)

    fourth_stage = conclusion_results(third_stage)
    print(fourth_stage)
