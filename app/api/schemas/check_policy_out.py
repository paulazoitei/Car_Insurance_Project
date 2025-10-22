from pydantic import BaseModel,ConfigDict
from datetime import date


class CheckPolicyOut(BaseModel):
    car_id:int
    date: date
    valid:bool

