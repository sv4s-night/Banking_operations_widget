import pandas as pd


def reading_file_csv_or_xlsx(path: str) -> pd.DataFrame:
    """Функция считывания финансовых операций из CSV- и XLSX-файлов."""
    if ".xlsx" in path:
        dframe = pd.read_excel(path)
        return dframe
    elif ".csv" in path:
        dframe = pd.read_csv(path)
        return dframe

