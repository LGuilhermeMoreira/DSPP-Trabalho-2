from sqlmodel import Field, Relationship, SQLModel
from typing import Optional, List


# Tabela de associação entre Comandas e Pratos
class ComandaPratoLink(SQLModel, table=True):
    id_comanda: Optional[int] = Field(default=None, foreign_key="comandas.id", primary_key=True)
    id_prato: Optional[int] = Field(default=None, foreign_key="pratos.id", primary_key=True)
    quantidade: int = Field(...)

# Tabela de associação entre Pratos e Ingredientes
class PratoIngredienteLink(SQLModel, table=True):
    id_prato: Optional[int] = Field(default=None, foreign_key="pratos.id", primary_key=True)
    id_ingrediente: Optional[int] = Field(default=None, foreign_key="ingredientes.id", primary_key=True)
    quantidade_utilizada: float = Field(...)
