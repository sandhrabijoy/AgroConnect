from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.server.routes.fcroutes import router as FCRouter
from app.server.database.database import Base,engine

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(FCRouter,tags=["farmercompany"],prefix="/farmer")

@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome to this fantastic app!"}