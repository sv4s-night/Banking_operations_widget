import logging

masks_logger = logging.getLogger("masks")
masks_logger.setLevel(logging.INFO)
file_handler = logging.FileHandler("../logs/masks.log")
file_formatter = logging.Formatter("%(asctime)s - %(filename)s - %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
masks_logger.addHandler(file_handler)


def get_mask_card_number(number_card: str) -> str:
    """Возвращает замаскированный номер карты"""
    masks_logger.info("function get_mask_card_number")
    return f"{str(number_card)[:4]} {str(number_card)[4:6]}** **** {str(number_card)[-4:]}"


def get_mask_account(account_number: str) -> str:
    """Возвращает замаскированный номер счета"""
    masks_logger.info("function get_mask_account")
    return f"XXXX{str(account_number)[-4:]}"
