from typing import Optional
from datetime import date,datetime
from pydantic import BaseModel,Field
from sqlalchemy.orm import relationship, sessionmaker,declarative_base,Session
from sqlalchemy import create_engine,Column,Integer,String, Boolean, DateTime
from app.server.database.database import Base

#ORM model for farmer company
class Farmer(Base):
    __tablename__='farmer_company'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    code=Column(Integer, nullable=False)
    active=Column(Boolean,nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    created_by = Column(String, nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)
    updated_by = Column(String, nullable=False)
    # Relationship to Cultivators
    cultivators = relationship("Cultivator", back_populates="farmer")


# Creation of initial farmer structure
class FarmerSchema(BaseModel):
    name: str
    code:int
    active:bool
    created_at: date
    created_by: str
    updated_at: date
    updated_by: str

    # Adding schema example
    class Config:
        orm_mode = True

# Update schema for PUT operation
class UpdatedFarmerSchema(BaseModel):
    name: Optional[str]
    code:Optional[int]
    active:Optional[bool]
    created_at: Optional[date]
    created_by: Optional[str]
    updated_at: Optional[date]
    updated_by: Optional[str]

    # Adding schema example
    class Config:
        orm_mode = True
        
#define the response messaage to be obtained
def ResponseModel(data, message):
    return {
        "data": [data],
        "code": 200,
        "message": message,
    }
#Define the error message to be obtained
def ErrorResponseModel(error, code, message):
    return {"error": error, "code": code, "message": message}