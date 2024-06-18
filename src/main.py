from src.masks import get_mask_account, get_mask_card_number
from src.widget import mask_account_card, get_data


if __name__ == "__main__":
    user_card_number = "Maestro 1596837868705199"     #input("Введите номер Вашей карты: ")
    print(get_mask_card_number(user_card_number))

    user_account = "Счет 64686473678894779589"         #input("Введите номер Вашего счета: ")
    print(get_mask_account(user_account))

    print("==================================================")

    info_card = "Maestro 1596837868705199"
    print(mask_account_card(info_card))

    info_data = "2018-07-11T02:26:18.671407"
    print(get_data(info_data))
