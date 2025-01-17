from typing import Optional
from datetime import date,datetime
from pydantic import BaseModel,Field
from sqlalchemy.orm import sessionmaker,declarative_base,Session
from sqlalchemy import create_engine,Column,Integer,String, Boolean, DateTime

Base=declarative_base()

#ORM model
class Farmer(Base):
    __tablename__:'farmercompany'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    code=Column(Integer, nullable=False)
    active=Column(Boolean,nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    created_by = Column(String, nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)
    updated_by = Column(String, nullable=False)


