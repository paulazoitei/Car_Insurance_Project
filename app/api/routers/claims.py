from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.api.schemas.claim_in import ClaimIn
from app.api.schemas.claim_out import ClaimOut
from app.db.session import get_db
from app.services.claim_service import ClaimService

router=APIRouter(tags=["claims"])
@router.post('/api/cars/{car_id}/claims',response_model=ClaimOut)
def add_claim(car_id:int,payload:ClaimIn,db:Session=Depends(get_db)):
    return ClaimService.create_claim(db,car_id,payload)
