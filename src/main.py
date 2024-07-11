# from src.generators import card_number_generator, filter_by_currency, transaction_descriptions
# from src.decorators import log
from src.utils import read_financial_transactions, checking_currency


if __name__ == "__main__":
    # transactions = [
    #     {
    #         "id": 939719570,
    #         "state": "EXECUTED",
    #         "date": "2018-06-30T02:08:58.425572",
    #         "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
    #         "description": "Перевод организации",
    #         "from": "Счет 75106830613657916952",
    #         "to": "Счет 11776614605963066702",
    #     },
    #     {
    #         "id": 142264268,
    #         "state": "EXECUTED",
    #         "date": "2019-04-04T23:20:05.206878",
    #         "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
    #         "description": "Перевод со счета на счет",
    #         "from": "Счет 19708645243227258542",
    #         "to": "Счет 75651667383060284188",
    #     },
    #     {
    #         "id": 873106923,
    #         "state": "EXECUTED",
    #         "date": "2019-03-23T01:09:46.296404",
    #         "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
    #         "description": "Перевод со счета на счет",
    #         "from": "Счет 44812258784861134719",
    #         "to": "Счет 74489636417521191160",
    #     },
    #     {
    #         "id": 895315941,
    #         "state": "EXECUTED",
    #         "date": "2018-08-19T04:27:37.904916",
    #         "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
    #         "description": "Перевод с карты на карту",
    #         "from": "Visa Classic 6831982476737658",
    #         "to": "Visa Platinum 8990922113665229",
    #     },
    #     {
    #         "id": 594226727,
    #         "state": "CANCELED",
    #         "date": "2018-09-12T21:27:25.241689",
    #         "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
    #         "description": "Перевод организации",
    #         "from": "Visa Platinum 1246377376343588",
    #         "to": "Счет 14211924144426031657",
    #     },
    # ]
    #
    # usd_transactions = filter_by_currency(transactions, "USD")
    # descriptions = transaction_descriptions(transactions)
    #
    # for element in range(3):
    #     print(next(usd_transactions)["id"])
    #     print(next(descriptions))
    #
    # for card_number in card_number_generator(1, 10):
    #     print(card_number)

    # ================================================ lesson 11.2
    #     @log(filename="mylog.txt")
    #     def my_function(x, y):
    #         return x / y
    #
    #     print(my_function(2, 2))
    #     print(my_function(1, 0))

    # ================================================ lesson 12.1


    file_path = '../data/operations.json'                        # путь до json файла
    transactions = read_financial_transactions(file_path)

    print(checking_currency(transactions, "RUB"))
