from app.server.database.cultivatordb import cultivator_company_helper,getCultivatorData
from app.server.database.cultivatordb import addCultivatorData,get_id_cultivator_company,update_cultivator_company,delete_company
from sqlalchemy.orm import Session
from app.server.database.database import get_db
from fastapi import APIRouter,Depends
from app.server.models.cultivatormodel import Cultivator,UpdatedCultivatorSchema,CultivatorSchema

router = APIRouter()

@router.get("/",response_description="Cultivator Data retrieved")
def get_cultivator_companies(db:Session = Depends(get_db)):
    cultivator_companies = getCultivatorData(db)
    if cultivator_companies:
        return [cultivator_company_helper(fc) for fc in cultivator_companies]
    


@router.post("/",response_description="Cultivator Data added successfully")
def add_farmer_company(data:CultivatorSchema, db:Session = Depends(get_db)):
    added = addCultivatorData(data.dict(),db)
    return added     

@router.get("/{id}",response_description="Cultivator retrieved")
def get_cultivator_company(id:int, db:Session = Depends(get_db)):
    cultivator_company = get_id_cultivator_company(db,id)
    if cultivator_company is not None:
        return cultivator_company_helper(cultivator_company)
    return "empty list returned: The data doesnt exist"

@router.put("/{id}", response_description= "Cultivator Data updated successfully")
def update_cultivator_company_data(id:int, req: UpdatedCultivatorSchema,db:Session = Depends(get_db)):
    req_data = {k:v for k, v in req.dict().items() if v is not None}
    if update_cultivator_company(db,id,req_data):
        updated_cultivator_company = get_id_cultivator_company(db,id)
        return cultivator_company_helper(updated_cultivator_company)     
    
@router.delete("/{id}",response_description="Cultivator Data deleted successfully")
def delete_cultivator_company(id:int, db:Session = Depends(get_db)):
    if delete_company(id,db):
        return f"Data with id {id} deleted sucessfully"
    else:
        return "Unable to delete cultivator data"