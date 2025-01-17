from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy import create_engine
from fastapi import Depends
from typing import Annotated

URL = "postgresql://postgres:Sandhra11$@host:5432/AgroConnect"
engine = create_engine(URL)
SessionLocal = sessionmaker(autocommit = False, autoflush = False, bind = engine)
Base = declarative_base()
def get_db():
    db = SessionLocal
    try:
        yield db
    finally:
        db.close()
db_dependency = Annotated[Session, Depends(get_db)]