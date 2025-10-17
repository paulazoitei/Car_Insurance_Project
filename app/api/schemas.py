from pydantic import BaseModel,ConfigDict,Field
from datetime import datetime
from typing import List

class OwnerOut(BaseModel):
    id: int
    name: str | None = None
    email: str | None = None

    model_config = ConfigDict(from_attributes=True)


class ClaimOut(BaseModel):
    id: int
    description: str | None = None
    created_at: datetime | None = None

    model_config = ConfigDict(from_attributes=True)


class InsurancePolicyOut(BaseModel):
    id: int
    provider: str | None = None
    start_date: datetime | None = None
    end_date: datetime | None = None

    model_config = ConfigDict(from_attributes=True)


class CarOut(BaseModel):
    id: int
    vin: str | None = None
    make: str | None = None
    model: str | None = None
    year_of_manufacture: int | None = None
    owner_id: int | None = None

    owner: OwnerOut | None = None
    claims: List[ClaimOut] = Field(default_factory=list)
    insurance_policies: List[InsurancePolicyOut] = Field(default_factory=list)

    model_config = ConfigDict(from_attributes=True)