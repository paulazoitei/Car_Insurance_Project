from sqlalchemy import ForeignKey
import datetime


from ..base import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import DateTime
from sqlalchemy.sql import func

class PolicyExpiryLog(Base):
    __tablename__="policy_expiry_log"
    id:Mapped[int]=mapped_column(primary_key=True)
    policy_id:Mapped[int]=mapped_column(ForeignKey("insurance_policy.id",ondelete="CASCADE"))
    expired_at: Mapped[datetime.datetime] = mapped_column(DateTime(timezone=True), nullable=False)
    created_at: Mapped[datetime.datetime] = mapped_column(DateTime(timezone=True), server_default=func.now(),
                                                          nullable=False)
    insurance_policy:Mapped["InsurancePolicy"]=relationship(back_populates="policy_expiry_logs")