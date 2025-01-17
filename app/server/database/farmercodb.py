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
