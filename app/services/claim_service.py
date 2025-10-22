from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.api.schemas.claim_in import ClaimIn
from app.db.models.car import Car

from app.db.models.claim import Claim


class ClaimService:
    @staticmethod
    def create_claim(db:Session, car_id:int, data:ClaimIn):

        car =db.get(Car,car_id)
        if not car:
            raise HTTPException(status_code=404,detail="Car not found")

        claim=Claim(
            car_id=car_id,
            claim_date=data.claim_date,
            description=data.description,
            amount=data.amount
        )

        db.add(claim)
        try:
            db.commit()
        except Exception as e:
            db.rollback()
            raise HTTPException(status_code=400, detail="Invalid claim payload") from e
        db.refresh(claim)
        return claim
