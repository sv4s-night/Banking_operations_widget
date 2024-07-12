from unittest.mock import patch

from src.external_api import currency_conversion


@patch("requests.request")
def test_currency_conversion(mock_requests):
    mock_requests.return_value.text = '{"from": "USD", "to": "RUB", "amount": 10}'
    assert currency_conversion("USD", "EUR", "10") == {"amount": 10, "from": "USD", "to": "RUB"}
