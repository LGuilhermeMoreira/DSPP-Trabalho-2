from typing import List, Optional
from sqlalchemy.orm import Session
from app.models import cliente as cliente_model
from app.dto import ClienteCreate, ClienteUpdate
from fastapi import HTTPException
from sqlmodel import select


def create_cliente(cliente_data: ClienteCreate, db: Session) -> cliente_model.Cliente:
    db_cliente = cliente_model.Cliente(**cliente_data.dict())
    db.add(db_cliente)
    db.commit()
    db.refresh(db_cliente)
    return db_cliente


def list_clientes(db: Session) -> List[cliente_model.Cliente]:
    clientes = db.exec(select(cliente_model.Cliente)).all()
    return clientes


def get_cliente(cliente_id: int, db: Session) -> cliente_model.Cliente:
    db_cliente = db.get(cliente_model.Cliente, cliente_id)
    if not db_cliente:
        raise HTTPException(status_code=404, detail="Cliente not found")
    return db_cliente


def update_cliente(cliente_id: int, cliente_data: ClienteUpdate, db: Session) -> cliente_model.Cliente:
    db_cliente = db.get(cliente_model.Cliente, cliente_id)
    if not db_cliente:
        raise HTTPException(status_code=404, detail="Cliente not found")
    for key, value in cliente_data.dict(exclude_unset=True).items():
        setattr(db_cliente, key, value)
    db.add(db_cliente)
    db.commit()
    db.refresh(db_cliente)
    return db_cliente


def delete_cliente(cliente_id: int, db: Session) -> bool:
    db_cliente = db.get(cliente_model.Cliente, cliente_id)
    if not db_cliente:
        raise HTTPException(status_code=404, detail="Cliente not found")
    db.delete(db_cliente)
    db.commit()
    return True