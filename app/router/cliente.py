from fastapi import APIRouter, Depends, HTTPException
from typing import List
from sqlalchemy.orm import Session
from app.models.all_models import Cliente as cliente_model
from app.dto.cliente import ClienteCreate, ClienteUpdate
from app.config.session_database import get_db
from app.controller.cliente import ClienteController

router = APIRouter()


@router.post("/clientes/", response_model=cliente_model)
def create_cliente(cliente_data: ClienteCreate, db: Session = Depends(get_db)):
    return ClienteController.create_cliente(cliente_data, db)


@router.get("/clientes/", response_model=List[cliente_model])
def list_clientes(db: Session = Depends(get_db)):
    return ClienteController.list_clientes(db)


@router.get("/clientes/{cliente_id}", response_model=cliente_model)
def get_cliente(cliente_id: int, db: Session = Depends(get_db)):
    return ClienteController.get_cliente(cliente_id, db)


@router.put("/clientes/{cliente_id}", response_model=cliente_model)
def update_cliente(cliente_id: int, cliente_data: ClienteUpdate, db: Session = Depends(get_db)):
    return ClienteController.update_cliente(cliente_id, cliente_data, db)


@router.delete("/clientes/{cliente_id}")
def delete_cliente(cliente_id: int, db: Session = Depends(get_db)):
    return {"ok": ClienteController.delete_cliente(cliente_id, db)}