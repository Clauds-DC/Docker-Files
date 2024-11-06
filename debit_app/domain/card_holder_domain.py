

class CardHolderDomain():

    def __init__(self, card_account_no:str, card_name: str, card_status: str) -> None:
       self.__card_account_no = card_account_no
       self.__card_name = card_name
       self.__card_status = card_status

    @property
    def card_account_no(self) -> str:
        return self.__card_account_no
    
    @card_account_no.setter
    def card_account_no(self, value:str) -> str:
        self.__card_account_no = value

    @property
    def card_name(self) -> str:
        return self.__card_name
    
    @card_name.setter
    def card_name(self, value:str):
        self.__card_name = value


    @property
    def card_status(self) -> str:
        return self.__card_status
    
    @card_status.setter
    def card_status(self, value:str):
        self.__card_status = value


    
    def to_dict(self) -> dict:
        return {
            "card_account_no": self.__card_account_no,
            "card_name": self.__card_name,
            "card_status": self.__card_status,
        }


