from models.farmercomodel import Farmer
from sqlalchemy.orm import Session
def farmer_company_helper(farmerData:Farmer) -> dict:
    return {
        "id":farmerData.id,
        "name":farmerData.name,
        "code":farmerData.code,
        "active":farmerData.active,
        "created_at": farmerData.created_at,
        "created_by": farmerData.created_by,
        "updated_at": farmerData.updated_at,
        "updated_by":  farmerData.updated_by,
    }
def getFarmerCompanyData(db:Session) ->Farmer:
    farmerData = db.query(Farmer).all()
    return farmerData

def addFarmerCompanyData(companyData:dict,db:Session)->Farmer:
    try:
        new_data = Farmer(**companyData)   
        db.add(new_data)
        db.commit()
        db.refresh(new_data)
        return new_data
    except:
        return "Unable to add the data to the database"
def update_farmer_company(db:Session,id:int,data:dict,)->bool:
        existing_farmer_company = db.query(Farmer).filter(Farmer.id == id).first()
        if not existing_farmer_company:
             return False
        for key, value in data.items():
             setattr(existing_farmer_company,key,value)
        db.commit()
        db.refresh(existing_farmer_company)
        return True             

def get_id_farmer_company(db:Session,id:int):
     farmer_company = db.query(Farmer).filter(Farmer.id == id).first()
     if farmer_company:
        return farmer_company
     return None
def delete_company(id:int,db:Session)->bool:
     existing_company = db.query(Farmer).filter(Farmer.id == id).first()
     if existing_company:
          db.delete(existing_company)
          db.commit()
          return True
     return False