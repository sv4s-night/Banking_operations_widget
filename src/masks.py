def get_mask_card_number(number_card: str) -> str:
    """Возвращает замаскированный номер карты"""

    if number_card.isdigit() and len(number_card) == 16:
        result = f" {str(number_card)[:4]} {str(number_card)[4:6]}** **** {str(number_card)[-4:]}"
    else:
        result = "Вы допустили ошибку при вводе данных карты"

    return result


def get_mask_account(account_number: str) -> str:
    """Возвращает замаскированный номер счета"""
    if account_number.isdigit():
        result = f" XXXX{str(account_number)[-4:]}"
    else:
        result = "Введены некорректные данные"

    return result
