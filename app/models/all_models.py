from typing import Optional, List
from sqlmodel import Field, Relationship, SQLModel

class ComandaPratoLink(SQLModel, table=True):
    id_comanda: Optional[int] = Field(default=None, foreign_key="comanda.id", primary_key=True)
    id_prato: Optional[int] = Field(default=None, foreign_key="prato.id", primary_key=True)
    quantidade: int = Field(...)

class PratoIngredienteLink(SQLModel, table=True):
    id_prato: Optional[int] = Field(default=None, foreign_key="prato.id", primary_key=True)
    id_ingrediente: Optional[int] = Field(default=None, foreign_key="ingrediente.id", primary_key=True)
    quantidade_utilizada: float = Field(...)

class Cliente(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    nome: str
    telefone: Optional[str]
    email: Optional[str]
    cpf: str
    # faminto : bool = Field(default=False)

    comandas: List["Comanda"] = Relationship(back_populates="cliente")

class Comanda(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    id_cliente: Optional[int] = Field(default=None, foreign_key="cliente.id")
    id_mesa: Optional[int] = Field(default=None, foreign_key="mesa.id", unique=True)
    data_hora_abertura: str
    data_hora_fechamento: Optional[str]
    status: str

    cliente: Optional["Cliente"] = Relationship(back_populates="comandas")
    mesa: Optional["Mesa"] = Relationship(back_populates="comanda")
    pratos: List["Prato"] = Relationship(back_populates="comandas", link_model= ComandaPratoLink) 

class Ingrediente(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    nome: str
    estoque: bool
    quantidade_estoque: float
    peso: float

    pratos: List["Prato"] = Relationship(back_populates="ingredientes", link_model=PratoIngredienteLink) 

class Mesa(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    numero_mesa: int = Field(unique=True)
    capacidade: int
    ocupada: bool = Field(default=False)
    numero_pessoas: Optional[int]
    comanda: Optional["Comanda"] = Relationship(back_populates="mesa", sa_relationship_kwargs={"uselist": False})

class Prato(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    nome: str
    preco: float
    descricao: Optional[str]
    disponivel: bool = Field(default=True)

    comandas: List["Comanda"] = Relationship(back_populates="pratos", link_model=ComandaPratoLink)
    ingredientes: List["Ingrediente"] = Relationship(back_populates="pratos", link_model=PratoIngredienteLink)
