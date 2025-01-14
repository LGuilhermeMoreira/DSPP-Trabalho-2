from fastapi import FastAPI
from app.router.cliente import router_cliente
from app.router.comanda import router_comanda
from app.router.ingrediente import router_ingrediente
from app.router.mesa import router_mesa
from app.router.prato import router_prato
app = FastAPI()

app.include_router(router_cliente, prefix="/cliente",tags=["cliente"])
app.include_router(router_mesa, prefix="/mesa",tags=["mesa"])
app.include_router(router_comanda, prefix="/comanda",tags=["comanda"])
app.include_router(router_ingrediente, prefix="/ingrediente",tags=["ingrediente"])
app.include_router(router_prato, prefix="/prato",tags=["prato"])


@app.get("/")
def read_root():
    return {"message": "API de Gerenciamento de Restaurante"}
