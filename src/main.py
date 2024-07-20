# from src.generators import card_number_generator, filter_by_currency, transaction_descriptions
# from src.decorators import log
# from src.external_api import checking_currency
# from src.masks import get_mask_account, get_mask_card_number
# from src.utils import read_financial_transactions
from src.financial import reader_file_transaction_csv, reader_file_transaction_excel
from src.processing import filter_by_state

if __name__ == "__main__":
    # ================================================ HW lesson 13.1 ===

    csv_file = "../data/transactions.csv"
    xlsx_file = "../data/transactions_excel.xlsx"

    xlsx_data = reader_file_transaction_excel(xlsx_file)
    csv_data = reader_file_transaction_csv(csv_file)

    # Вывод только транзакций PENDING (рассматриваемые)
    print(filter_by_state(csv_data, "PENDING"))
