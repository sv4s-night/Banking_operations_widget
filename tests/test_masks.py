from src.masks import get_mask_card_number, get_mask_account


def test_get_mask_card_number(fixture_test_mask_account_card):
    assert get_mask_card_number(fixture_test_mask_account_card) == "1111 22** **** 4444"


def test_get_mask_account(fixture_test_get_mask_account):
    assert get_mask_account(fixture_test_get_mask_account) == "XXXX4321"
