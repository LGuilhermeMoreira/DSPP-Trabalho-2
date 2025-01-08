from pydantic import BaseModel
class IngredienteCreate(BaseModel):
    nome: str
    estoque: bool

class IngredienteUpdate(BaseModel):
    nome: str | None
    estoque:bool | None
