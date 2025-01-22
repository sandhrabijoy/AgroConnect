from typing import Optional
from datetime import date,datetime
from pydantic import BaseModel,Field
from sqlalchemy.orm import relationship,sessionmaker,declarative_base,Session
from sqlalchemy import create_engine,Column,Integer,String, Boolean, DateTime,ForeignKey

Base=declarative_base()

#ORM model for cultivator
class Cultivator(Base):
    __tablename__='cultivator'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    companyid=Column(Integer,ForeignKey("farmer_company.id") ,nullable=False)
    active=Column(Boolean,nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    created_by = Column(String, nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)
    updated_by = Column(String, nullable=False)
    # Relationship to Farmer
    farmer = relationship("Farmer", back_populates="cultivators")


# Creation of initial cultivator structure
class CultivatorSchema(BaseModel):
    name: str
    companyid:int
    active:bool
    created_at: date
    created_by: str
    updated_at: date
    updated_by: str

    # Adding schema example
    class Config:
        orm_mode = True

# Update schema for PUT operation
class UpdatedCultivatorSchema(BaseModel):
    name: Optional[str]
    companyid:Optional[int]
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