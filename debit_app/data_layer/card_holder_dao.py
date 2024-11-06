import json
from util.utils import Utils
from domain.card_holder_domain import CardHolderDomain


class CardHolderDetailsDao():

    def __init__(self) -> None:
        self._data_file_name = "card_holder_details.json"
        self._utils = Utils()

    def get_all_card_holders(self) -> list:
        with open(f"./data/{self._data_file_name}", 'r') as file:
            card_holder_details = json.load(file)

            return self._utils.convert_card_account_details_to_domain(card_holder_details)
        
    def update_card_holders(self, card_holder_details: list):

        with open(f"./data/{self._data_file_name}", 'w') as file:
            json.dump(self._utils.convert_card_account_details_to_json(card_holder_details), file, indent=2)

        print(f"Data has been written to {self._data_file_name}")

    def get_card_holder_by_account_no(self, card_account_number: str) -> CardHolderDomain:

        card_holders = self.get_all_card_holders()
        for card_holder in card_holders:
            if card_holder.card_account_no == card_account_number:
                return card_holder
            
        return None
    

        
        


if __name__ == "__main__":

    card_holder_dao = CardHolderDetailsDao()
    print(f"card_holders_list: {json.dumps(card_holder_dao.get_all_card_holders(), indent=2)}")