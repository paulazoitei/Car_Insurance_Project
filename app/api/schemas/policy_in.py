from datetime import datetime
from pydantic import BaseModel, field_validator, model_validator

class InsurancePolicyCreate(BaseModel):
    provider: str | None = None
    start_date: datetime
    end_date: datetime

    @field_validator("provider")
    @classmethod
    def provider_not_empty(cls, v: str | None):
        if v is None or v.strip() == "":
            raise ValueError("provider cannot be empty")
        return v

    @model_validator(mode="after")
    def check_dates(self):
        if self.end_date is None:
            raise ValueError("end_date is required")
        if self.end_date < self.start_date:
            raise ValueError("end_date must be greater than or equal to start_date")
        return self
