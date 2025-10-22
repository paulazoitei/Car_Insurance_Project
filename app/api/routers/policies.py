

from fastapi import APIRouter, Query, Depends
from datetime import date as Date

from sqlalchemy.orm import Session
from starlette import status

from app.api.schemas.check_policy_out import CheckPolicyOut
from app.api.schemas.policy_in import InsurancePolicyCreate
from app.api.schemas.policy_out import InsurancePolicyOut
from app.db.session import  get_db

from app.services.policy_service import PolicyService

router=APIRouter(tags=["policies"])
@router.get('/api/cars/{car_id}/insurance-valid',response_model=CheckPolicyOut)
def check_insurance_validity(car_id:int,date:Date=Query(...),db:Session=Depends(get_db)):
    return PolicyService.check_insurance_validity_service(car_id, date, db)


@router.post("/api/cars/{car_id}/policies", response_model=InsurancePolicyOut, status_code=status.HTTP_201_CREATED)
def add_policy(car_id: int, payload: InsurancePolicyCreate, db: Session= Depends(get_db)):
    return PolicyService.create_policy(db, car_id, payload)