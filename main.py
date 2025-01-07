from fastapi import FastAPI
from app.router.cliente import router as cliente_router

app = FastAPI()
app.include_router(cliente_router, prefix="/api")

@app.get("/")
def read_root():
    return {"message": "API de Gerenciamento de Restaurante"}
