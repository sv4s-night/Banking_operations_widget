from src.masks import get_mask_card_number, get_mask_account
import pytest


def test_get_mask_card_number(fixture_test_mask_account_card):
    assert get_mask_card_number(fixture_test_mask_account_card) == "1111 22** **** 4444"


@pytest.mark.parametrize('account_number, result', [
    ('5555666688889999', 'XXXX9999'),
    ('1111222244445555', 'XXXX5555')])
def test_mark_parametrize(account_number, result):
    assert get_mask_account(account_number) == result
