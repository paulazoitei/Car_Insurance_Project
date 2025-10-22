from datetime import datetime

from pydantic import BaseModel, ConfigDict
from decimal import Decimal


class ClaimOut(BaseModel):
    id: int
    car_id:int
    claim_date: datetime
    description: str
    amount :Decimal
    model_config = ConfigDict(from_attributes=True,arbitrary_types_allowed=True)

