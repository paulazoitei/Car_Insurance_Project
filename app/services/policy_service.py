
from fastapi import HTTPException
from sqlalchemy import select, and_
from sqlalchemy.orm import Session

from app.db.models.car import Car
from app.db.models.insurance_policy import InsurancePolicy
from app.api.schemas.policy_in import InsurancePolicyCreate
from datetime import date




class PolicyService:
    @staticmethod
    def create_policy(db: Session, car_id: int, data: InsurancePolicyCreate) :

        car = db.get(Car, car_id)
        if not car:
            raise HTTPException(status_code=404, detail="Car not found")

        overlap_stmt = select(InsurancePolicy).where(
            and_(
                InsurancePolicy.car_id == car_id,
                InsurancePolicy.start_date <= data.end_date,
                InsurancePolicy.end_date >= data.start_date,
            )
        )
        if db.scalar(overlap_stmt):
            raise HTTPException(status_code=409, detail="New policy overlaps an existing policy")


        policy = InsurancePolicy(
            car_id=car_id,
            provider=data.provider,
            start_date=data.start_date,
            end_date=data.end_date,
        )

        db.add(policy)
        try:
            db.commit()
        except Exception:
            db.rollback()
            raise
        db.refresh(policy)
        return policy
    @staticmethod
    def check_insurance_validity_service(car_id:int,day:date,db:Session):
        year=day.year
        if year < 1900 or year > 2100:
            raise HTTPException(400, "Year out of range")
        car = select(InsurancePolicy).where(
            InsurancePolicy.car_id == car_id,
            InsurancePolicy.start_date <= day,
            InsurancePolicy.end_date >= day
        )
        policy = db.scalar(car)

        if not policy:
            raise HTTPException(404, "No valid insurance policy for that date.")

        return {"car_id":car_id,"date":day,"valid":True}
