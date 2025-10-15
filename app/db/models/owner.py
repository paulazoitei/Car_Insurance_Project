from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from sqlalchemy import String
from typing import List
from ..base import Base
from car import Car

class Owner(Base):
   __tablename__ ="owner"
   id :Mapped[int]=mapped_column(primary_key=True)
   name: Mapped[String]=mapped_column(String(50),nullable=False)
   email:Mapped[String]=mapped_column(String(50),nullable=True)
   cars:Mapped[List["Car"]]=relationship(back_populates="owner",cascade="all, delete-orphan")
