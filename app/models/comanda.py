from typing import Optional, List
from sqlmodel import Field, Relationship, SQLModel

class Comanda(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    id_cliente: Optional[int] = Field(default=None, foreign_key="cliente.id")
    id_mesa: Optional[int] = Field(default=None, foreign_key="mesa.id", unique=True)
    data_hora_abertura: str  # Pode ser substituído por um tipo datetime, dependendo do uso
    data_hora_fechamento: Optional[str]
    status: str

    cliente: Optional["Cliente"] = Relationship(back_populates="comandas")
    mesa: Optional["Mesa"] = Relationship(back_populates="comanda")
    pratos: List["Prato"] = Relationship(back_populates="comandas", link_model="ComandaPratoLink")