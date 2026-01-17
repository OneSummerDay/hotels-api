from typing import List
from app.database import Base
from sqlalchemy import JSON, Column, ForeignKey, Integer, String

class Room(Base):
    __tablename__ = "rooms"

    id = Column(Integer, primary_key=True, index=True)
    hotel_id = Column(ForeignKey("hotels.id"), nullable=False)
    neme = Column(String, nullable=False)
    description = Column(String)
    price = Column(Integer)
    services = JSON(List)
    quantity = Column(Integer)
    image = Column(Integer)