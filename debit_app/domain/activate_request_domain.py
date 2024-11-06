from pydantic import BaseModel, Field
from typing import Literal

class ActivateRequestDomain(BaseModel):
    card_account_no: str = Field(description="Name of new User", min_length=2)
    card_status: Literal['activate', 'deactivate'] = Field(description="Target Status of Card: activate or deactivate")