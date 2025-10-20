

from fastapi import APIRouter, Query, Depends, HTTPException
from datetime import date
from app.db.session import  get_db
from sqlalchemy import select
from app.db.models.insurance_policy import  InsurancePolicy

router=APIRouter()
@router.get('api/cars/{car_id}/insurance-valid')
def check_insurance_validity(car_id:int,date:date=Query(...),db=Depends(get_db)):

    if not date:
        raise  HTTPException(400,"Bad format for date")
    year=date.year
    if year <1900 or year >2100:
        raise HTTPException(400,"Year out of range")


    car=select(InsurancePolicy).where(
        InsurancePolicy.car_id==car_id
    )
    policy=db.scalar(car)

    if not policy:
        raise HTTPException(404,"No valid insurance policy for this car.")

    return {"car_id":car_id,"date":date,"valid":True}