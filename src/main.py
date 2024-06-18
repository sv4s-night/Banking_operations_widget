from .masks import get_mask_account, get_mask_card_number

if __name__ == "__main__":
    user_card_number = input("Введите номер Вашей карты: ")
    print(get_mask_card_number(user_card_number))

    user_account = input("Введите номер Вашего счета: ")
    print(get_mask_account(user_account))
