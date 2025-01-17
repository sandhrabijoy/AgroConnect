from app.server.models.cultivatormodel import Cultivator
from sqlalchemy.orm import Session

def cultivator_company_helper(CultivatorData:Cultivator) -> dict:
    return {
        "id":CultivatorData.id,
        "companyid":CultivatorData.companyid,
        "name":CultivatorData.name,
        "active":CultivatorData.active,
        "created_at": CultivatorData.created_at,
        "created_by": CultivatorData.created_by,
        "updated_at": CultivatorData.updated_at,
        "updated_by":  CultivatorData.updated_by,
    }

def getCultivatorData(db:Session) ->Cultivator:
    CultivatorData = db.query(Cultivator).all()
    return CultivatorData

def addCultivatorData(companyData:dict,db:Session)->Cultivator:
    try:
        new_data = Cultivator(**companyData)   
        db.add(new_data)
        db.commit()
        db.refresh(new_data)
        return new_data
    except:
        return "Unable to add the data to the database"
    
def update_cultivator_company(db:Session,id:int,data:dict,)->bool:
        existing_cultivator_company = db.query(Cultivator).filter(Cultivator.id == id).first()
        if not existing_cultivator_company:
             return False
        for key, value in data.items():
             setattr(existing_cultivator_company,key,value)
        db.commit()
        db.refresh(existing_cultivator_company)
        return True             

def get_id_cultivator_company(db:Session,id:int):
     cultivator_company = db.query(Cultivator).filter(Cultivator.id == id).first()
     if cultivator_company:
        return cultivator_company
     return None

def delete_company(id:int,db:Session)->bool:
     existing_company = db.query(Cultivator).filter(Cultivator.id == id).first()
     if existing_company:
          db.delete(existing_company)
          db.commit()
          return True
     return False