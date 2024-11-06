from data_layer.card_holder_dao import CardHolderDetailsDao
from util.utils import Utils
from domain.card_holder_domain import CardHolderDomain

class CardHolderBll():

    def __init__(self) -> None:
        self._card_holder_dao = CardHolderDetailsDao()
        self._utils = Utils()

    def register_user_account(self, card_name:str) -> CardHolderDomain:
        
        # Get ALL card holders record from json file
        current_card_holders = self._card_holder_dao.get_all_card_holders()
        while True:
            new_card_account_no = self._utils.generate_card_uuid()
            # Check if there's duplicate acc num, loop again to generate if duplicate
            if not self._utils.is_current_account_number_exists(current_card_holders, new_card_account_no):
                break

        # Create new user account detail
        new_account_detail =  CardHolderDomain(new_card_account_no, card_name, "activated")
        
        # Append new User
        current_card_holders.append(new_account_detail)

        # Insert to Local json file
        self._card_holder_dao.update_card_holders(current_card_holders)

        return new_account_detail
    

    def is_card_holder_exists(self, card_account_no:str) -> CardHolderDomain:
        return self._card_holder_dao.get_card_holder_by_account_no(card_account_no)

    def activate_deactivate_account(self, card_account_no:str, card_status:str) -> True:
        
        updated_card_holders = []
        card_holders = self._card_holder_dao.get_all_card_holders()

        for card_holder in card_holders:

            if card_holder.card_account_no == card_account_no:
                card_holder.card_status = card_status

            updated_card_holders.append(card_holder)

        self._card_holder_dao.update_card_holders(updated_card_holders)

        return True




if __name__ == "__main__":

    card_holder_bll = CardHolderBll()
    print(f"isduplicate: {card_holder_bll.register_user_account}")


