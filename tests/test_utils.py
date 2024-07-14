from src.utils import read_financial_transactions


def test_read_financial_transactions(fixture_test_read_financial_transactions):
    assert read_financial_transactions(fixture_test_read_financial_transactions) == []
