from pydantic import BaseModel

class ComandaCreate(BaseModel):
    id_cliente: int | None
    id_mesa: int | None
    data_hora_abertura: str
    data_hora_fechamento: str | None
    status: str

class ComandaUpdate(BaseModel):
    id_cliente: int | None
    id_mesa: int | None
    data_hora_abertura: str | None
    data_hora_fechamento: str | None
    status: str | None