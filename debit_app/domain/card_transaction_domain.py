
class CardTransactionDomain():

    def __init__(self, card_account_no:str, txn_date: str, txn_type: str, txn_amount: float, txn_description:str ) -> None:
       self.__card_account_no = card_account_no
       self.__txn_date = txn_date
       self.__txn_type = txn_type
       self.__txn_amount = txn_amount
       self.__txn_description = txn_description

    @property
    def card_account_no(self) -> str:
        return self.__card_account_no
    
    @card_account_no.setter
    def card_account_no(self, value:str) -> str:
        self.__card_account_no = value

    @property
    def txn_date(self) -> str:
        return self.__txn_date
    
    @txn_date.setter
    def txn_date(self, value:str) -> str:
        self.__txn_date = value

    @property
    def txn_type(self) -> str:
        return self.__txn_type
    
    @txn_type.setter
    def txn_type(self, value:str) -> str:
        self.__txn_type = value

    @property
    def txn_amount(self) -> float:
        return self.__txn_amount
    
    @txn_amount.setter
    def txn_amount(self, value:float) -> float:
        self.__txn_amount = value

    @property
    def txn_description(self) -> str:
        return self.__txn_description
    
    @txn_description.setter
    def txn_description(self, value:str) -> str:
        self.__txn_description = value

    def to_dict(self) -> dict:
        return  {
            "card_account_no": self.__card_account_no,
            "txn_date": self.__txn_date,
            "txn_type": self.__txn_type,
            "txn_amount": self.__txn_amount,
            "txn_description": self.__txn_description
        }