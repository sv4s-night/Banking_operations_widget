from src.widget import mask_account_card, get_data

if __name__ == "__main__":
    get_user_info = str(input("Введите данные Вашей карты или счета:\n"))
    print(mask_account_card(get_user_info))

    info_data = str(input("Введите дату операции:\n"))
    print(get_data(info_data))
