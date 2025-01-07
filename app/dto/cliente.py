from pydantic import BaseModel

class ClienteCreate(BaseModel):
    nome: str
    telefone: str  
    email:  str |  None

class ClienteUpdate(BaseModel):
    nome: str | None
    telefone: str | None
    email: str | None