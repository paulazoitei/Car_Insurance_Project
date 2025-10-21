from pydantic import BaseModel,ConfigDict,Field
from datetime import datetime
from typing import List
from app.api.schemas.policy_out import InsurancePolicyOut
from app.api.schemas.owner_out import OwnerOut
from app.api.schemas.claim_out import ClaimOut



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