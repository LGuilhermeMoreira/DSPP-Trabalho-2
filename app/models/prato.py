from typing import Optional, List
from sqlmodel import Field, Relationship, SQLModel

class Prato(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    nome: str
    preco: float
    descricao: Optional[str]

    comandas: List["Comanda"] = Relationship(back_populates="pratos", link_model="ComandaPratoLink")
    ingredientes: List["Ingrediente"] = Relationship(back_populates="pratos", link_model="PratoIngredienteLink")
