
from sqlalchemy.orm import Mapped,mapped_column
from sqlalchemy import String,ForeignKey
from ..base import Base
from owner import Owner

class Car(Base):
    __tablename__="car"
    id:Mapped[int]=mapped_column(primary_key=True)
    vin:Mapped[String]=mapped_column(String(17),nullable=False,unique=True)
    make:Mapped[String]=mapped_column(String(50),nullable=True)
    model:Mapped[String]=mapped_column(String(50),nullable=True)
    year_of_manufacture:Mapped[int]=mapped_column()
    owner_id:Mapped[int]=mapped_column(ForeignKey("owner.id"))
