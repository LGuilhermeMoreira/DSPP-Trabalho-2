from fastapi import APIRouter, Depends, Query
from typing import Dict, Any, Optional
from sqlalchemy.orm import Session
from app.models.all_models import Cliente as cliente_model
from app.dto.cliente import ClienteCreate, ClienteUpdate
from app.config.database import get_db
from app.controller.cliente import ClienteController

router_cliente = APIRouter()

@router_cliente.post("/", response_model=cliente_model)
def create_cliente(cliente_data: ClienteCreate, db: Session = Depends(get_db)):
    return ClienteController.create_cliente(cliente_data, db)

@router_cliente.get("/", response_model=Dict[str, Any])
def list_clientes(
    page: int = Query(1, description="Número da página", ge=1),
    limit: int = Query(10, description="Número de itens por página", ge=1),
    nome: Optional[str] = Query(None, description="Filtrar por nome"),
    email: Optional[str] = Query(None, description="Filtrar por email"),
    cpf: Optional[str] = Query(None, description="Filtrar por CPF"),
    db: Session = Depends(get_db)
):
    return ClienteController.list_clientes(db, page=page, limit=limit, nome=nome, email=email, cpf=cpf)

@router_cliente.get("/{cliente_id}", response_model=cliente_model)
def get_cliente(cliente_id: int, db: Session = Depends(get_db)):
    return ClienteController.get_cliente(cliente_id, db)


@router_cliente.put("/{cliente_id}", response_model=cliente_model)
def update_cliente(cliente_id: int, cliente_data: ClienteUpdate, db: Session = Depends(get_db)):
    return ClienteController.update_cliente(cliente_id, cliente_data, db)


@router_cliente.delete("/{cliente_id}")
def delete_cliente(cliente_id: int, db: Session = Depends(get_db)):
    return {"ok": ClienteController.delete_cliente(cliente_id, db)}

@router_cliente.get("/num")
def get_num_clientes(db: Session = Depends(get_db)):
    return ClienteController.num_cliente(db)