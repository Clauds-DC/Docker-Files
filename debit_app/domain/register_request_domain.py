from pydantic import BaseModel, Field

class RegisterRequestDomain(BaseModel):
    card_name: str = Field(description="Name of new User", min_length=2)