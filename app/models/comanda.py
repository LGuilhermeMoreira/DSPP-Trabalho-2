from sqlmodel import Field, Relationship, SQLModel
from typing import Optional, List
from models.cliente import Cliente
from models.mesa import Mesa
from models.prato import Prato
from models.link import ComandaPratoLink

class Comanda(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    id_cliente: Optional[int] = Field(default=None, foreign_key="clientes.id")
    id_mesa: Optional[int] = Field(default=None, foreign_key="mesas.id", unique=True)
    data_hora_abertura: str  # Pode ser substituído por um tipo datetime, dependendo do uso
    data_hora_fechamento: Optional[str]
    status: str
    
    cliente: Optional[Cliente] = Relationship(back_populates="comandas")
    mesa: Optional[Mesa] = Relationship(back_populates="comanda")
    pratos: List["Prato"] = Relationship(back_populates="comandas", link_model=ComandaPratoLink)
