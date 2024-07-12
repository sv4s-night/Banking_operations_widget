from unittest.mock import patch

from src.utils import checking_currency, read_financial_transactions


def test_read_financial_transactions(fixture_test_read_financial_transactions):
    assert read_financial_transactions(fixture_test_read_financial_transactions) == []


@patch("src.external_api.currency_conversion")
def test_checking_currency(mock_checking, fixture_test_checking_currency):
    mock_checking.return_value = 8221.37
    assert checking_currency(fixture_test_checking_currency, "RUB") == 8221.37
    mock_checking.assert_called_once_with("RUB", "USD", "8221.37")
