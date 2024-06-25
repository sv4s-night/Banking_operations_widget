from src.widget import mask_account_card, get_data


def test_mask_account_card(fixture_test_mask_account_card):
    assert mask_account_card(fixture_test_mask_account_card) == " 1111 22** **** 4444"


def test_get_data(fixture_test_get_data):
    assert get_data(fixture_test_get_data) == '12.09.2018'
