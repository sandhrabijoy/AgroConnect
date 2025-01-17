from database.farmercodb import farmer_company_helper,getFarmerCompanyData,addFarmerCompanyData
from sqlalchemy.orm import Session
from database.database import get_db
from fastapi import APIRouter,Depends
from models.farmercomodel import Farmer

router = APIRouter()

@router.get("/",response_description="Data retrieved")
def get_farmer_companies(db:Session = Depends(get_db)):
    farmer_companies = getFarmerCompanyData(db)
    if farmer_companies:
        return [farmer_company_helper(fc) for fc in farmer_companies]
    
@router.post("/",response_description="Data added successfully")
def add_farmer_company(data:Farmer, db:Session = Depends(get_db)):
    added = addFarmerCompanyData(data.dict(),db)
    return added     