from typing import Optional, List
from sqlmodel import Field, Relationship, SQLModel

class Ingrediente(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    nome: str
    estoque: float

    pratos: List["Prato"] = Relationship(back_populates="ingredientes", link_model="PratoIngredienteLink")