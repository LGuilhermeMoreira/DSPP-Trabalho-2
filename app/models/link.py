from sqlmodel import Field, SQLModel
from typing import Optional

class ComandaPratoLink(SQLModel, table=True):
    id_comanda: Optional[int] = Field(default=None, foreign_key="comanda.id", primary_key=True)
    id_prato: Optional[int] = Field(default=None, foreign_key="prato.id", primary_key=True)
    quantidade: int = Field(...)

class PratoIngredienteLink(SQLModel, table=True):
    id_prato: Optional[int] = Field(default=None, foreign_key="prato.id", primary_key=True)
    id_ingrediente: Optional[int] = Field(default=None, foreign_key="ingrediente.id", primary_key=True)
    quantidade_utilizada: float = Field(...)
