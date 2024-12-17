from backend.database import Base
from sqlalchemy import Column, String, Float, Integer, DateTime
from sqlalchemy.sql import func

class Acc_PriceDB(Base):
    __tablename__ = "accommodation_price"
    id = Column(Integer,primary_key=True,autoincrement=True)
    name = Column(String,unique=True)
    price = Column(Float)
    tier = Column(Integer)
    min_price = Column(Float)
    base_price = Column(Float)
    created_at = Column(DateTime(timezone=True), default=func.now())

