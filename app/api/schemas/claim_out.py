from datetime import datetime

from pydantic import BaseModel, ConfigDict


class ClaimOut(BaseModel):
    id: int
    description: str | None = None
    created_at: datetime | None = None

    model_config = ConfigDict(from_attributes=True)

