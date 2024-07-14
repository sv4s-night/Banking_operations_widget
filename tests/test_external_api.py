from unittest.mock import patch

from src.external_api import checking_currency


@patch("requests.request")
def test_checking_currency(mock_requests, fixture_test_checking_currency):
    mock_requests.return_value.text = '{"from": "USD", "to": "RUB", "amount": 10}'
    assert checking_currency(fixture_test_checking_currency) == {"amount": 10, "from": "USD", "to": "RUB"}
    mock_requests.assert_called_once_with(
        "GET",
        "https://api.apilayer.com/exchangerates_" "data/convert?to=RUB&from=USD&amount=8221.37",
        headers={"apikey": "None"},
        data={},
    )
