from pydantic import BaseModel, Field

class CardTransactionRequestDomain(BaseModel):
    card_account_no: str = Field(description="Target account number of user history", min_lengt=14, max_length=14)
    