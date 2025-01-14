from typing import List, Optional
from sqlalchemy.orm import Session
from app.models.all_models import Mesa as mesa_model
from app.dto.mesa import MesaCreate, MesaUpdate
from fastapi import HTTPException
from sqlmodel import select

class MesaController:
    @staticmethod
    def create_mesa(mesa_data: MesaCreate, db: Session) -> mesa_model:
        try:
            db_mesa = mesa_model(**mesa_data.model_dump())
            db.add(db_mesa)
        except Exception as e:
            db.rollback()
            raise HTTPException(status_code=500, detail=str(e))
        finally:
            db.commit()
            db.refresh(db_mesa)
            return db_mesa

    @staticmethod
    def list_mesas(db: Session) -> List[mesa_model]:
        try:
            mesas = db.execute(select(mesa_model)).scalars().all()
        except Exception as e:
            db.rollback()
            raise HTTPException(status_code=500, detail=str(e))
        finally:
            return mesas

    @staticmethod
    def get_mesa(mesa_id: int, db: Session) -> mesa_model:
        try:
            mesa = db.get(mesa_model, mesa_id)
            if not mesa:
                raise HTTPException(status_code=404, detail="Mesa not found")
        except Exception as e:
            db.rollback()
            raise HTTPException(status_code=500, detail=str(e))
        finally:
            return mesa

    @staticmethod
    def update_mesa(mesa_id: int, mesa_data: MesaUpdate, db: Session) -> mesa_model:
        try:
            db_mesa = db.get(mesa_model, mesa_id)
            if not db_mesa:
                raise HTTPException(status_code=404, detail="Mesa not found")
            for key, value in mesa_data.model_dump(exclude_unset=True).items():
                setattr(db_mesa, key, value)
            db.add(db_mesa)
        except Exception as e:
            db.rollback()
            raise HTTPException(status_code=500, detail=str(e))
        finally:
            db.commit()
            db.refresh(db_mesa)
            return db_mesa

    @staticmethod
    def delete_mesa(mesa_id: int, db: Session) -> bool:
        try:
            db_mesa = db.get(mesa_model, mesa_id)
            if not db_mesa:
                raise HTTPException(status_code=404, detail="Mesa not found")
        except Exception as e:
            db.rollback()
            raise HTTPException(status_code=500, detail=str(e))
        finally:
            db.delete(db_mesa)
            db.commit()
            return True
    
    @staticmethod
    def num_mesa(db: Session) -> int:
        try:
            num = db.execute(select(mesa_model)).count()
        except Exception as e:
            db.rollback()
            raise HTTPException(status_code=500, detail=str(e))
        finally:
            return {"quantiade" : num}