import random
from domain.card_holder_domain import CardHolderDomain
from domain.card_transaction_domain import CardTransactionDomain
from datetime import datetime


class Utils():

   

    def generate_card_uuid(self) -> str:
        # Generate a random 12-digit number
        number = ''.join([str(random.randint(0, 9)) for _ in range(12)])
        
        # Format the number with hyphens every 4 digits
        formatted_number = f"{number[:4]}-{number[4:8]}-{number[8:]}"
        
        return formatted_number
    

    def is_current_account_number_exists(self, card_holders:list, card_account_no:str) -> bool:
        
        for card_holder in card_holders:
            if card_account_no == card_holder.card_account_no:
                return True
            
        return False
    
    def convert_card_account_details_to_domain(self, card_holders:list) -> list:
        card_holder_domain_list = []
        for card_holder in card_holders:
            card_holder_domain_list.append(CardHolderDomain(
                card_holder['card_account_no'],
                card_holder['card_name'],
                card_holder['card_status']
            ))

        return card_holder_domain_list
    
    
    def convert_card_account_details_to_json(self, card_holders:list) -> list:
        card_holder_domain_list = []
        for card_holder in card_holders:
            card_holder_domain_list.append(card_holder.to_dict())

        return card_holder_domain_list
    
    def convert_card_transaction_details_to_json(self, card_transactions:list) -> list:
        card_transaction_domain_list = []
        for card_transaction in card_transactions:
            card_transaction_domain_list.append(card_transaction.to_dict())

        return card_transaction_domain_list

    def convert_card_transaction_details_to_domain(self, card_transactions:list) -> list:
        card_transaction_domain_list = []
        for card_transaction in card_transactions:
            card_transaction_domain_list.append(CardTransactionDomain(
                card_transaction['card_account_no'],
                card_transaction['txn_date'],
                card_transaction['txn_type'],
                card_transaction['txn_amount'],
                card_transaction['txn_description']

            ))

        return card_transaction_domain_list
    

    def get_specific_account_history(self, card_transactions:list, card_account_no:str):

        consolidated_card_transactions = []

        # Loop to all card transactions and append only specific account txn
        for card_transaction in card_transactions:
            if card_account_no == card_transaction.card_account_no:
                consolidated_card_transactions.append(card_transaction)
        
        return consolidated_card_transactions
    
    def get_account_balance(self, account_transactions:list) -> float:
        card_balance = 0.0

        for transaction in account_transactions:
            if transaction.txn_type == "debit":
                card_balance = card_balance - transaction.txn_amount
            else: 
                card_balance = card_balance + transaction.txn_amount

        return card_balance
    

    def generate_date_time_string(self, format_str: str = "%Y-%m-%d %H:%M:%S") -> str:
        """
        Generates a string representing the current date and time.

        Args:
            format_str (str): The format string to use for the date and time representation.
                            Defaults to "%Y-%m-%d %H:%M:%S" (e.g., "2024-09-15 14:30:00").

        Returns:
            str: The formatted date and time string.
        """
        # Get the current date and time
        now = datetime.now()
        
        # Format the date and time as a string using the provided format
        formatted_date_time = now.strftime(format_str)
        
        return formatted_date_time



if __name__ == "__main__":
    utils = Utils()
    print(f"generate_card_uuid: {utils.generate_card_uuid()}")

