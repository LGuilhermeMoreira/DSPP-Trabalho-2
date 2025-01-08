from pydantic import BaseModel
class PratoCreate(BaseModel):
    nome: str
    preco: float
    descricao:  str | None

class PratoUpdate(BaseModel):
    nome:  str | None
    preco: float | None
    descricao:  str | None
