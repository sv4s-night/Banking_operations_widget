def get_mask_card_number(number_card: str) -> str:
    """Возвращает замаскированный номер карты"""
    return f"{str(number_card)[:4]} {str(number_card)[4:6]}** **** {str(number_card)[-4:]}"


def get_mask_account(account_number: str) -> str:
    """Возвращает замаскированный номер счета"""
    return f"XXXX{str(account_number)[-4:]}"
