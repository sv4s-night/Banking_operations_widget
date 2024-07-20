from src.financial import reader_file_transaction_csv, reader_file_transaction_excel
from src.processing import filter_by_state

if __name__ == "__main__":

    # HW lesson 13.1
    csv_file = "../data/transactions.csv"
    xlsx_file = "../data/transactions_excel.xlsx"

    xlsx_data = reader_file_transaction_excel(xlsx_file)
    csv_data = reader_file_transaction_csv(csv_file)

    # Вывод только транзакций PENDING (рассматриваемые)
    print(filter_by_state(csv_data, "PENDING"))
