from pydantic import BaseModel
class MesaCreate(BaseModel):
    numero_mesa: int
    capacidade: int
    ocupada: bool

class MesaUpdate(BaseModel):
    numero_mesa: int | None
    capacidade: int | None
    ocupada: bool | None