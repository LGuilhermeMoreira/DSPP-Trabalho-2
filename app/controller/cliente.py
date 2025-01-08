from typing import List, Optional
from sqlalchemy.orm import Session
from app.models.all_models import Cliente as cliente_model
from app.dto.cliente import ClienteCreate, ClienteUpdate
from fastapi import HTTPException
from sqlmodel import select

class ClienteService:
    @staticmethod
    def create_cliente(cliente_data: ClienteCreate, db: Session) -> cliente_model:
        try:
            db_cliente = cliente_model(**cliente_data.model_dump())
            db.add(db_cliente)
            db.commit()
            db.refresh(db_cliente)
            return db_cliente
        except Exception as e:
            return e
            

    @staticmethod
    def list_clientes(db: Session) -> List[cliente_model]:
        clientes = db.execute(select(cliente_model)).scalars().all()
        return clientes

    @staticmethod
    def get_cliente(cliente_id: int, db: Session) -> cliente_model:
        db_cliente = db.get(cliente_model, cliente_id)
        if not db_cliente:
            raise HTTPException(status_code=404, detail="Cliente not found")
        return db_cliente

    @staticmethod
    def update_cliente(cliente_id: int, cliente_data: ClienteUpdate, db: Session) -> cliente_model:
        db_cliente = db.get(cliente_model, cliente_id)
        if not db_cliente:
            raise HTTPException(status_code=404, detail="Cliente not found")
        for key, value in cliente_data.dict(exclude_unset=True).items():
            setattr(db_cliente, key, value)
        db.add(db_cliente)
        db.commit()
        db.refresh(db_cliente)
        return db_cliente

    @staticmethod
    def delete_cliente(cliente_id: int, db: Session) -> bool:
        db_cliente = db.get(cliente_model, cliente_id)
        if not db_cliente:
            raise HTTPException(status_code=404, detail="Cliente not found")
        db.delete(db_cliente)
        db.commit()
        return True