import pandas as pd
import json


def reading_financial_transactions_csv(path: str, response_format: str = dict):
    """ Функция считывает финансовые операции из CSV файла"""
    dframe = pd.read_csv(path)

    if response_format == "json":
        return dframe.to_json(orient="records")
    else:
        return dframe.to_dict()


def reading_financial_transactions_xlsx(path: str) -> pd.DataFrame:
    """ Функция считывает финансовые операции из XLSX файла"""
    dframe = pd.read_excel(path)
    return pd.DataFrame(dframe)
    # return dframe.to_dict()
