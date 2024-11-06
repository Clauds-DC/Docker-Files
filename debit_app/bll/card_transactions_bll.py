from data_layer.card_holder_dao import CardHolderDetailsDao
from data_layer.card_transaction_dao import CardTransactionDao
from util.utils import Utils
from domain.card_transaction_domain import CardTransactionDomain
from domain.card_insert_transaction_request_domain import CardInsertTransactionRequestDomain

class CardTransactionsBll():

    def __init__(self) -> None:
        self._card_holder_dao = CardHolderDetailsDao()
        self._card_transaction_dao = CardTransactionDao()
        self._utils = Utils()

    def get_account_history(self, card_account_no:str) -> list:

        # get all history
        all_account_history = self._card_transaction_dao.get_all_account_transaction()

        # filter account history
        account_history = self._utils.get_specific_account_history(all_account_history, card_account_no)
        return account_history
    
    def get_account_balance(self, account_transactions:list) -> float:
        return self._utils.get_account_balance(account_transactions)
    

    def check_transaction_if_valid(self, request_transaction: CardInsertTransactionRequestDomain) -> bool:
        
        # Check if requested amount is lessthan account balance
        if request_transaction.transaction_type == 'credit':
            print(f"if {request_transaction.transaction_amount} < {self.get_account_balance(self.get_account_history(request_transaction.card_account_no))}:")
            if request_transaction.transaction_amount < self.get_account_balance(self.get_account_history(request_transaction.card_account_no)):
                return False
        
        return True
        
    def insert_transaction(self, card_account_no:str, request_transaction: CardInsertTransactionRequestDomain) -> CardTransactionDomain:

        # get all history
        all_account_history = self._card_transaction_dao.get_all_account_transaction()

        # Build new transaction
        new_transaction = CardTransactionDomain(card_account_no,
                                                self._utils.generate_date_time_string(),
                                                request_transaction.transaction_type,
                                                request_transaction.transaction_amount,
                                                request_transaction.transaction_description)
        all_account_history.append(new_transaction)

        # Insert to file
        self._card_transaction_dao.update_account_transactions(all_account_history)

        return new_transaction
