from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.server.routes.fcroutes import router as FCRouter
from app.server.database.database import Base,engine
from app.server.routes.routes_cultivator import router as CultivatorRouter
app = FastAPI()

Base.metadata.create_all(bind=engine)

origins=[
"http://localhost:3000",
"http://localhost:8000",

]
app.add_middleware(
CORSMiddleware,
allow_origins=["http://localhost:5173"],
allow_credentials=True,
allow_methods=["*"],  
allow_headers=["*"],  
)

app.include_router(FCRouter,tags=["farmercompany"],prefix="/farmer")
app.include_router(CultivatorRouter,tags=["cultivator"],prefix="/cultivator")
@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome to this fantastic app!"}