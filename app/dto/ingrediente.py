from pydantic import BaseModel
class PratoCreate(BaseModel):
    nome: str
    preco: float
    descricao: Optional[str] = None

class PratoUpdate(BaseModel):
    nome: Optional[str] = None
    preco: Optional[float] = None
    descricao: Optional[str] = None