import pytest


@pytest.fixture
def fixture_test_processing():
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]


@pytest.fixture
def fixture_test_mask_account_card():
    return "1111222233334444"


@pytest.fixture
def fixture_test_get_data():
    return "2018-09-12T21:27:25.241689"


@pytest.fixture
def fixture_test_get_mask_account():
    return "12345678900987654321"





