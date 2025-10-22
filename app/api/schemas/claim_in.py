from pydantic import BaseModel,field_validator,ConfigDict,Field
from datetime import datetime
from decimal import Decimal

class ClaimIn(BaseModel):
    claim_date: datetime
    description: str
    amount: Decimal

    @field_validator("claim_date")
    @classmethod
    def check_claim_date(cls,v:datetime|None):
        if v is None:
            raise ValueError("claim date cannot be empty")
        if v > datetime.now():
            raise ValueError("claim cannot be in future")
        return v
    @field_validator("description")
    @classmethod
    def check_description(cls,v:str|None):
        if v is None:
            raise ValueError("description cannot be empty")
        return v

    @field_validator("amount")
    @classmethod
    def check_amount(cls,v:Decimal|None):
        if v is None:
            raise ValueError("amount cannot be empty")
        if v<Decimal(0):
            raise ValueError("amount need to be positive")
        return v

