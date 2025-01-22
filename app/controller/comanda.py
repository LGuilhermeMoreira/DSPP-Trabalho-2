from typing import List, Optional
from sqlalchemy.orm import Session
from app.models.all_models import Comanda as comanda_model
from app.dto.comanda import ComandaCreate, ComandaUpdate
from fastapi import HTTPException
from sqlmodel import select

class ComandaController:
    @staticmethod
    def create_comanda(comanda_data: ComandaCreate, db: Session) -> comanda_model:
        try:
            db_comanda = comanda_model(**comanda_data.model_dump())
            db.add(db_comanda)
        except Exception as e:
            db.rollback()
            raise HTTPException(status_code=500, detail=str(e))
        finally:
            db.commit()
            db.refresh(db_comanda)
            return db_comanda

    @staticmethod
    def list_comandas(db: Session) -> List[comanda_model]:
        try:
            comandas = db.execute(select(comanda_model)).scalars().all()
        except Exception as e:
            db.rollback()
            raise HTTPException(status_code=500, detail=str(e))
        finally:
            return comandas

    @staticmethod
    def get_comanda(comanda_id: int, db: Session) -> comanda_model:
        try:
            comanda = db.get(comanda_model, comanda_id)
            if not comanda:
                raise HTTPException(status_code=404, detail="Comanda not found")
        except Exception as e:
            db.rollback()
            raise HTTPException(status_code=500, detail=str(e))
        finally:
            return comanda

    @staticmethod
    def update_comanda(comanda_id: int, comanda_data: ComandaUpdate, db: Session) -> comanda_model:
        try:
            db_comanda = db.get(comanda_model, comanda_id)
            if not db_comanda:
                raise HTTPException(status_code=404, detail="Comanda not found")
            for key, value in comanda_data.model_dump(exclude_unset=True).items():
                setattr(db_comanda, key, value)
            db.add(db_comanda)
        except Exception as e:
            db.rollback()
            raise HTTPException(status_code=500, detail=str(e))
        finally:
            db.commit()
            db.refresh(db_comanda)
            return db_comanda

    @staticmethod
    def delete_comanda(comanda_id: int, db: Session) -> bool:
        try:
            db_comanda = db.get(comanda_model, comanda_id)
            if not db_comanda:
                 raise HTTPException(status_code=404, detail="Comanda not found")
        except Exception as e:
            db.rollback()
            raise HTTPException(status_code=500, detail=str(e))
        finally:
            db.delete(db_comanda)
            db.commit()
            return True

    @staticmethod
    def num_comanda(db: Session) -> int:
        try:
            num = db.execute(select(comanda_model)).count()
        except Exception as e:
            db.rollback()
            raise HTTPException(status_code=500, detail=str(e))
        finally:
            return {"quantiade" : num}
    
    #filtro por relacionamento
    @staticmethod
    def listar_comandas_por_cliente(db: Session, cliente_id: int):
        try:
            statement = select(comanda_model).where(comanda_model.id_cliente == cliente_id)
            comandas = db.exec(statement).all()
        except Exception as e:
            db.rollback()
            raise HTTPException(status_code=500, detail=str(e))
        finally:
            return comandas