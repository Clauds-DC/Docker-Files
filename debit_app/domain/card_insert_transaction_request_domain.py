from pydantic import BaseModel, Field, confloat
from typing import Literal

class CardInsertTransactionRequestDomain(BaseModel):
    card_account_no: str = Field(description="Target account number of user", min_lengt=14, max_length=14)
    transaction_amount: confloat(gt=0) = Field(description="Transaction Amount")
    transaction_type: Literal['debit', 'credit'] = Field(description="transaction type: debit or credit")
    transaction_description: str = Field(description="Transaction Description")