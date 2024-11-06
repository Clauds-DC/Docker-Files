from fastapi import FastAPI
from domain.default_response_domain import DefaultResponse
from domain.register_request_domain import RegisterRequestDomain
from domain.activate_request_domain import ActivateRequestDomain
from domain.card_transaction_request import CardTransactionRequestDomain
from domain.card_insert_transaction_request_domain import CardInsertTransactionRequestDomain
from bll.card_holder_bll import CardHolderBll
from bll.card_transactions_bll import CardTransactionsBll

from util.utils import Utils

card_holder_bll = CardHolderBll()
card_transactions_bll = CardTransactionsBll()
utils = Utils()

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


"""
    Inserts transactions
    Checks if account exists, if active and balance is sufficient
"""
@app.post("/transaction")
async def insert_transaction(request: CardInsertTransactionRequestDomain):

    card_holder_detail = card_holder_bll.is_card_holder_exists(request.card_account_no)
    # Test if existing
    if not card_holder_detail:
        response = DefaultResponse(status="fail", 
                                   data={"card_account_no": request.card_account_no}, 
                                   code=400,
                                   message="'card_account_no' does not exists"
                                   )
        return response
    
    # Check if activated
    # Check status
    if not card_holder_detail.card_status == 'activated':
        response = DefaultResponse(status="fail", 
                            data={"card_status": request.card_status}, 
                            code=400,
                            message=f"account '{request.card_account_no}' is 'deactivated'."
                            )
        return response
    
    # Check transaction balance
    if not card_transactions_bll.check_transaction_if_valid(request):
        return DefaultResponse(status="fail", 
                    data={}, 
                    code=400,
                    message=f"Insufficient Account Balance. '' "
                    )

    # Insert transaction
    inserted_transaction = card_transactions_bll.insert_transaction(card_holder_detail.card_account_no, request)

    # Return updated details
    account_history = card_transactions_bll.get_account_history(request.card_account_no)
    transaction_summary = {
        "card_balance": card_transactions_bll.get_account_balance(account_history),
        "latest_transaction_details": inserted_transaction.to_dict()
    }
    
    response = DefaultResponse(status="success", 
                               data=transaction_summary, 
                               code=200)
    return response

"""
    gets transactions history and returns history with account balance and details
    Checks if account exists, if active
"""
@app.post("/transaction/history")
async def transaction_history(request: CardTransactionRequestDomain):

    card_holder_detail = card_holder_bll.is_card_holder_exists(request.card_account_no)
    # Test if existing
    if not card_holder_detail:
        response = DefaultResponse(status="fail", 
                                   data={"card_account_no": request.card_account_no}, 
                                   code=400,
                                   message="'card_account_no' does not exists"
                                   )
        return response
    
    # Check if activated
    # Check status
    if not card_holder_detail.card_status == 'activated':
        response = DefaultResponse(status="fail", 
                            data={"card_status": request.card_status}, 
                            code=400,
                            message=f"account '{request.card_account_no}' is 'deactivated'."
                            )
        return response
    
    account_history = card_transactions_bll.get_account_history(request.card_account_no)

    account_history_with_details = card_holder_detail.to_dict()
    account_history_with_details['card_balance'] = card_transactions_bll.get_account_balance(account_history)
    account_history_with_details['transactions'] = utils.convert_card_transaction_details_to_json(account_history)

    response = DefaultResponse(status="success", 
                               data=account_history_with_details, 
                               code=200)
    return response

"""
    Registers new USer
    Returns registered user with auto generated account number
    Checks if account number generated is duplicated
"""
@app.post("/register")
async def register_user(request: RegisterRequestDomain):

    new_card_holder_detail = card_holder_bll.register_user_account(request.card_name)

    response = DefaultResponse(status="success", data=new_card_holder_detail.to_dict(), code=200)
    return response

"""
    Activates existing user
    Returns updated user details
    Checks if account number exists and status is not equal to current state of user
"""
@app.post("/activate")
async def activate_user(request: ActivateRequestDomain):

    card_holder_detail = card_holder_bll.is_card_holder_exists(request.card_account_no)

    if request.card_status == 'activate':
        card_status = 'activated'
    else:
        card_status = 'deactivated'

    # Test if existing
    if not card_holder_detail:
        response = DefaultResponse(status="fail", 
                                   data={"card_account_no": request.card_account_no}, 
                                   code=400,
                                   message="'card_account_no' does not exists"
                                   )
        return response
    
    # Check status
    if card_holder_detail.card_status == card_status:
        response = DefaultResponse(status="fail", 
                            data={"card_status": request.card_status}, 
                            code=400,
                            message=f"account '{request.card_account_no}' is already set to '{request.card_status}' status"
                            )
        return response
    
    card_holder_bll.activate_deactivate_account(request.card_account_no, card_status)

    # set updated status
    card_holder_detail.card_status = card_status
    response = DefaultResponse(status="success",
                               message=f"Account successfully '{card_status}'",
                               data=card_holder_detail.to_dict(), 
                               code=200)
    return response
