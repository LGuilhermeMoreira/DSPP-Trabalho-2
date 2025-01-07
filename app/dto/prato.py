from pydantic import BaseModel
class IngredienteCreate(BaseModel):
    nome: str
    estoque: float

class IngredienteUpdate(BaseModel):
    nome: Optional[str] = None
    estoque: Optional[float] = None