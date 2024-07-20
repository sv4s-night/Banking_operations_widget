# import pandas as pd
# import pytest
# from src.financial import reader_file_transaction_csv, reader_file_transaction_excel
#
#
# @pytest.fixture
# def financial_csv():
#     sample_dict = {'id;state;date;amount;currency_name;currency_code;from;to;description':
#                        {
#                            0: '650703;EXECUTED;2023-09-05T11:30:32Z;16210;Sol;PEN;'
#                               'Счет 58803664561298323391;Счет 39745660563456619397;Перевод организации',
#                            1: '3598919;EXECUTED;2020-12-06T23:00:58Z;29740;Peso;COP;'
#                               'Discover 3172601889670065;Discover 0720428384694643;Перевод с карты на карту',
#                            2: '593027;CANCELED;2023-07-22T05:02:01Z;30368;Shilling;TZS;'
#                               'Visa 1959232722494097;Visa 6804119550473710;Перевод с карты на карту'}}
#
#     return pd.DataFrame(sample_dict)
#
