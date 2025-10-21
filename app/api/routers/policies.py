

from fastapi import APIRouter, Query, Depends, HTTPException
from datetime import date

from sqlalchemy.orm import Session
from starlette import status

from app.api.schemas.policy_in import InsurancePolicyCreate
from app.api.schemas.policy_out import InsurancePolicyOut
from app.db.session import  get_db
from sqlalchemy import select
from app.db.models.insurance_policy import  InsurancePolicy
from app.services.policy_service import create_policy

router=APIRouter(tags=["policies"])
@router.get('/api/cars/{car_id}/insurance-valid')
def check_insurance_validity(car_id:int,date:date=Query(...),db=Depends(get_db)):


    year=date.year
    if year <1900 or year >2100:
        raise HTTPException(400,"Year out of range")


    car=select(InsurancePolicy).where(
        InsurancePolicy.car_id==car_id,
        InsurancePolicy.start_date <=date,
        InsurancePolicy.end_date>=date
    )
    policy=db.scalar(car)

    if not policy:
        raise HTTPException(404,"No valid insurance policy for that date.")

    return {"car_id":car_id,"date":date,"valid":True}

@router.post("/api/cars/{car_id}/policies", response_model=InsurancePolicyOut, status_code=status.HTTP_201_CREATED)
def add_policy(car_id: int, payload: InsurancePolicyCreate, db: Session= Depends(get_db)):
    return create_policy(db, car_id, payload)