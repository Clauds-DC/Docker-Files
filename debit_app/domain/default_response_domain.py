from pydantic import BaseModel

class DefaultResponse(BaseModel):
    status: str
    message: str | None = None
    data: dict
    code: int