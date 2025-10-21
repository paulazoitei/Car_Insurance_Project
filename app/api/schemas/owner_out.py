from pydantic import BaseModel, ConfigDict


class OwnerOut(BaseModel):
    id: int
    name: str | None = None
    email: str | None = None

    model_config = ConfigDict(from_attributes=True)