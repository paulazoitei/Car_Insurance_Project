from datetime import datetime
from pydantic import BaseModel, ConfigDict

class InsurancePolicyOut(BaseModel):
    id: int
    car_id: int
    provider: str | None = None
    start_date: datetime
    end_date: datetime

    model_config = ConfigDict(from_attributes=True)

