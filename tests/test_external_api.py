from unittest.mock import patch

from src.external_api import currency_conversion


@patch("requests.request")
def test_currency_conversion(mock_requests, fixture_test_currency_conversion):
    mock_requests.return_value.text = '{"from": "USD", "to": "RUB", "amount": 10}'
    assert currency_conversion(fixture_test_currency_conversion) == {"from": "USD", "to": "RUB", "amount": 10}
