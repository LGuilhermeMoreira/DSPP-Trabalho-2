from sqlmodel import Field, Relationship, SQLModel
from typing import Optional, List
from models.prato import Prato
from models.link import PratoIngredienteLink
class Ingrediente(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    nome: str
    estoque: float
    
    pratos: List[Prato] = Relationship(back_populates="ingredientes", link_model=PratoIngredienteLink)