from sqlmodel import Field, Relationship, SQLModel
from typing import Optional
# from app.models.comanda import Comanda
# from .comanda import Comanda

class Mesa(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    numero_mesa: int = Field(unique=True)
    capacidade: int
    ocupada: bool = Field(default=False)
    
    comanda: Optional["Comanda"] = Relationship(back_populates="mesa", sa_relationship_kwargs={"uselist": False})
