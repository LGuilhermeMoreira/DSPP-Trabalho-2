from typing import List, Optional
from sqlalchemy.orm import Session
from app.models.all_models import Cliente as cliente_model
from app.dto.cliente import ClienteCreate, ClienteUpdate
from fastapi import HTTPException
from sqlmodel import select

class ClienteController:
    @staticmethod
    def create_cliente(cliente_data: ClienteCreate, db: Session) -> cliente_model:
        try:
            db_cliente = cliente_model(**cliente_data.model_dump())
            db.add(db_cliente)
        except Exception as e:           
            db.rollback()
            raise HTTPException(status_code=500, detail=str(e))
        finally:
            db.commit()
            db.refresh(db_cliente)
            return db_cliente      

    @staticmethod
    def list_clientes(db: Session) -> List[cliente_model]:
        try:
            clientes = db.execute(select(cliente_model)).scalars().all()
        except Exception as e:
            db.rollback()
            raise HTTPException(status_code=500, detail=str(e))
        finally:
            return clientes

    @staticmethod
    def get_cliente(cliente_id: int, db: Session) -> cliente_model:
        try:
            cliente = db.get(cliente_model, cliente_id)
            if not cliente:
                raise HTTPException(status_code=404, detail="Cliente not found")
        except Exception as e:
            db.rollback()
            raise HTTPException(status_code=500, detail=str(e))
        finally:
            return cliente  

    @staticmethod
    def update_cliente(cliente_id: int, cliente_data: ClienteUpdate, db: Session) -> cliente_model:
        try:
            db_cliente = db.get(cliente_model, cliente_id)
            if not db_cliente:
                raise HTTPException(status_code=404, detail="Cliente not found")
            for key, value in cliente_data.model_dump(exclude_unset=True).items():
                setattr(db_cliente, key, value)
            db.add(db_cliente)
        except Exception as e:
            db.rollback()
            raise HTTPException(status_code=500, detail=str(e))
        finally:
            db.commit()
            db.refresh(db_cliente)
            return db_cliente

    @staticmethod
    def delete_cliente(cliente_id: int, db: Session) -> bool:
        try:
            db_cliente = db.get(cliente_model, cliente_id)
            if not db_cliente:
                raise HTTPException(status_code=404, detail="Cliente not found")
        except Exception as e:
            db.rollback()
            raise HTTPException(status_code=500, detail=str(e))
        finally:
            db.delete(db_cliente)
            db.commit()
            return True