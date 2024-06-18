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


def mask_account_card(mask_info_card: srt) -> list:
    """Функция общей маскировки карты и счета"""
    masquerade = list()

    for x in mask_info_card:



    return masquerade





def get_data(date_str: str) -> str:
    """Функция преобразования даты"""

    parts = date_str.split('T')[0].split('-')
    return f"{parts[2]}.{parts[1]}.{parts[0]}"
