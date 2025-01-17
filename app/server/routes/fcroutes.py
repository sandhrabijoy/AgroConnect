from app.server.database.farmercodb import farmer_company_helper,getFarmerCompanyData
from app.server.database.farmercodb import addFarmerCompanyData,get_id_farmer_company,update_farmer_company,delete_company
from sqlalchemy.orm import Session
from app.server.database.database import get_db
from fastapi import APIRouter,Depends
from app.server.models.farmercomodel import Farmer,UpdatedFarmerSchema,FarmerSchema

router = APIRouter()

@router.get("/",response_description="Data retrieved")
def get_farmer_companies(db:Session = Depends(get_db)):
    farmer_companies = getFarmerCompanyData(db)
    if farmer_companies:
        return [farmer_company_helper(fc) for fc in farmer_companies]
    
@router.post("/",response_description="Data added successfully")
def add_farmer_company(data:FarmerSchema, db:Session = Depends(get_db)):
    added = addFarmerCompanyData(data.dict(),db)
    return added     

@router.get("/{id}",response_description="Farmer Company retrieved")
def get_farmer_company(id:int, db:Session = Depends(get_db)):
    farmer_company = get_id_farmer_company(db,id)
    if farmer_company is not None:
        return farmer_company_helper(farmer_company)
    return "empty list returned: The data doesnt exist"

@router.put("/{id}", response_description= "Data updated successfully")
def update_farmer_company_data(id:int, req: UpdatedFarmerSchema,db:Session = Depends(get_db)):
    req_data = {k:v for k, v in req.dict().items() if v is not None}
    if update_farmer_company(db,id,req_data):
        updated_farmer_company = get_id_farmer_company(db,id)
        return farmer_company_helper(updated_farmer_company)     
    
@router.delete("/{id}",response_description="Data deleted successfully")
def delete_farmer_company(id:int, db:Session = Depends(get_db)):
    if delete_company(id,db):
        return f"Data with id {id} deleted sucessfully"
    else:
        return "Unable to delete data"