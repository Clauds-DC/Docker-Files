import json
from util.utils import Utils
from domain.card_transaction_domain import CardTransactionDomain

class CardTransactionDao():

    def __init__(self) -> None:
        self._data_file_name = "transactions_details.json"
        self._utils = Utils()

    def get_all_account_transaction(self) -> list:
        with open(f"./data/{self._data_file_name}", 'r') as file:
            card_transaction_details = json.load(file)

            return self._utils.convert_card_transaction_details_to_domain(card_transaction_details)
        

    def update_account_transactions(self, transactions: list):

        with open(f"./data/{self._data_file_name}", 'w') as file:
            json.dump(self._utils.convert_card_transaction_details_to_json(transactions), file, indent=2)

        print(f"Data has been written to {self._data_file_name}")