"""
Функция принимает на вход только один аргумент — строку, которая состоит из требуемых частей.
Это может быть строка типа Visa Platinum 7000 7922 8960 6361,
или Maestro 7000 7922 8960 6361,
или Счет 73654108430135874305.
Разделять строку на 2 аргумента (отдельно имя, отдельно номер) нельзя!

========================================================================================================

Возвращать исходную строку с замаскированным номером карты/счета.
Для карты и счета используйте разные маскировки.

========================================================================================================

"""

from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(mask_info_card):
    """Функция общей маскировки карты и счета"""

    masquerade = mask_info_card.split(' ')

    for account_or_card in masquerade:
        if account_or_card.isdigit():
            if len(account_or_card) <= 16:
                result = masquerade[0] + get_mask_card_number(account_or_card)
            elif len(account_or_card) > 16:
                result = masquerade[0] + get_mask_account(account_or_card)
            else:
                result = "error"


    return result





def get_data(date_str: str) -> str:
    """Функция преобразования даты"""

    parts = date_str.split('T')[0].split('-')
    return f"{parts[2]}.{parts[1]}.{parts[0]}"
