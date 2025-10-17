import datetime
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String,ForeignKey,DateTime

from app.db.models.policy_expiry_log import PolicyExpiryLog
from..base import Base
from typing import List

class InsurancePolicy(Base):
    __tablename__="insurance_policy"
    id: Mapped[int] = mapped_column(primary_key=True)
    car_id: Mapped[int] = mapped_column(ForeignKey("car.id",ondelete="CASCADE"))
    car:Mapped["Car"]=relationship(back_populates="insurance_policies")
    provider:Mapped[String]=mapped_column(String(50),nullable=True)
    star_date:Mapped[datetime.datetime]=mapped_column(DateTime(timezone=True),nullable=False)
    end_date:Mapped[datetime.datetime]=mapped_column(DateTime(timezone=True),nullable=False)
    policy_expiry_logs:Mapped[List["PolicyExpiryLog"]]=relationship(back_populates="insurance_policy",cascade="all, delete-orphan")