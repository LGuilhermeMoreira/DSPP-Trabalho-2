from fastapi import APIRouter, Depends, HTTPException
from typing import List
from sqlalchemy.orm import Session
from app.models.cliente import Cliente as cliente_model
from app.dto.cliente import ClienteCreate, ClienteUpdate
from app.config.database import get_db
from app.controller.cliente import ClienteService

router = APIRouter()


@router.post("/clientes/", response_model=cliente_model)
def create_cliente(cliente_data: ClienteCreate, db: Session = Depends(get_db)):
    return ClienteService.create_cliente(cliente_data, db)


@router.get("/clientes/", response_model=List[cliente_model])
def list_clientes(db: Session = Depends(get_db)):
    return ClienteService.list_clientes(db)


@router.get("/clientes/{cliente_id}", response_model=cliente_model)
def get_cliente(cliente_id: int, db: Session = Depends(get_db)):
    return ClienteService.get_cliente(cliente_id, db)


@router.put("/clientes/{cliente_id}", response_model=cliente_model)
def update_cliente(cliente_id: int, cliente_data: ClienteUpdate, db: Session = Depends(get_db)):
    return ClienteService.update_cliente(cliente_id, cliente_data, db)


@router.delete("/clientes/{cliente_id}")
def delete_cliente(cliente_id: int, db: Session = Depends(get_db)):
    return {"ok": ClienteService.delete_cliente(cliente_id, db)}