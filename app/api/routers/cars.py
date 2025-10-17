
from fastapi import APIRouter,Depends
from sqlalchemy import select
from app.db.session import get_db
from app.db.models.car import Car

from app.api.schemas import CarOut


router=APIRouter()
@router.get('/api/cars',response_model=list[CarOut])
def get_cars(db=Depends(get_db)):
    cars=select(Car)
    result=db.scalars(cars).all()
    return result