import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


def test_filter_by_currency(fixture_test_filter_by_currency):
    usd_transactions = filter_by_currency(fixture_test_filter_by_currency, "RUB")
    for element in range(1):
        assert str(next(usd_transactions)["id"]) == "594226727"


def test_transaction_descriptions(fixture_test_transaction_descriptions):
    for iterated_object in transaction_descriptions(fixture_test_transaction_descriptions):
        assert iterated_object == "Перевод организации"


@pytest.mark.parametrize("start,stop,result", [(1, 1, "0000 0000 0000 0001"),
                                               (2, 2, "0000 0000 0000 0002")])
def test_card_number_generator(start, stop, result):
    for card_number in card_number_generator(start, stop):
        assert card_number == result
