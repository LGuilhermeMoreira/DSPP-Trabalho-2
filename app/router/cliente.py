from fastapi import APIRouter, Depends, HTTPException
from typing import List
from sqlalchemy.orm import Session
from app.models import cliente as cliente_model
from app.dto import ClienteCreate, ClienteUpdate
from app.config.database import get_db
from app.controller import cliente_controller

router = APIRouter()


@router.post("/clientes/", response_model=cliente_model.Cliente)
def create_cliente(cliente_data: ClienteCreate, db: Session = Depends(get_db)):
    return cliente_controller.create_cliente(cliente_data, db)


@router.get("/clientes/", response_model=List[cliente_model.Cliente])
def list_clientes(db: Session = Depends(get_db)):
    return cliente_controller.list_clientes(db)


@router.get("/clientes/{cliente_id}", response_model=cliente_model.Cliente)
def get_cliente(cliente_id: int, db: Session = Depends(get_db)):
    return cliente_controller.get_cliente(cliente_id, db)


@router.put("/clientes/{cliente_id}", response_model=cliente_model.Cliente)
def update_cliente(cliente_id: int, cliente_data: ClienteUpdate, db: Session = Depends(get_db)):
    return cliente_controller.update_cliente(cliente_id, cliente_data, db)


@router.delete("/clientes/{cliente_id}")
def delete_cliente(cliente_id: int, db: Session = Depends(get_db)):
    return {"ok": cliente_controller.delete_cliente(cliente_id, db)}