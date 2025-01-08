from typing import Optional, List
from sqlmodel import Field, Relationship, SQLModel
# from .comanda import Comanda
class Cliente(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    nome: str
    telefone: Optional[str]
    email: Optional[str]

    comandas: List["Comanda"] = Relationship(back_populates="cliente")
