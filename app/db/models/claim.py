import datetime

from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey,DateTime,Text,Index,DECIMAL
from sqlalchemy.sql import func
from ..base import Base



class Claim(Base):
    __tablename__="claim"
    id:Mapped[int]=mapped_column(primary_key=True)
    car_id:Mapped[int]=mapped_column(ForeignKey("car.id",ondelete="CASCADE"))
    car:Mapped["Car"]=relationship(back_populates="claims")
    claim_date:Mapped[datetime.datetime]=mapped_column(DateTime(timezone=True),nullable=False)
    description:Mapped[str]=mapped_column(Text,nullable=False)
    amount:Mapped[DECIMAL]=mapped_column(DECIMAL(12,2),nullable=False)
    created_at:Mapped[datetime.datetime]=mapped_column(DateTime(timezone=True),server_default=func.now(),nullable=False)

    __table_args__ = (
        Index("claim_index","car_id","claim_date"),
    )
