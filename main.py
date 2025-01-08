from fastapi import FastAPI
from app.router.cliente import router as cliente_router
from app.config.init_db import create_db_and_tables
app = FastAPI()
create_db_and_tables()
app.include_router(cliente_router, prefix="/api")

@app.get("/")
def read_root():
    return {"message": "API de Gerenciamento de Restaurante"}
