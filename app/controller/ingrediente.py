from typing import List, Optional
from sqlalchemy.orm import Session
from app.models.all_models import Ingrediente as ingrediente_model
from app.dto.ingrediente import IngredienteCreate, IngredienteUpdate
from fastapi import HTTPException
from sqlmodel import select

class IngredienteController:
    @staticmethod
    def create_ingrediente(ingrediente_data: IngredienteCreate, db: Session) -> ingrediente_model:
        try:
            db_ingrediente = ingrediente_model(**ingrediente_data.model_dump())
            db.add(db_ingrediente)
        except Exception as e:
            db.rollback()
            raise HTTPException(status_code=500, detail=str(e))
        finally:
            db.commit()
            db.refresh(db_ingrediente)
            return db_ingrediente

    @staticmethod
    def list_ingredientes(db: Session) -> List[ingrediente_model]:
        try:
            ingredientes = db.execute(select(ingrediente_model)).scalars().all()
        except Exception as e:
            db.rollback()
            raise HTTPException(status_code=500, detail=str(e))
        finally:
            return ingredientes

    @staticmethod
    def get_ingrediente(ingrediente_id: int, db: Session) -> ingrediente_model:
        try:
            ingrediente = db.get(ingrediente_model, ingrediente_id)
            if not ingrediente:
                raise HTTPException(status_code=404, detail="Ingrediente not found")
        except Exception as e:
            db.rollback()
            raise HTTPException(status_code=500, detail=str(e))
        finally:
            return ingrediente

    @staticmethod
    def update_ingrediente(ingrediente_id: int, ingrediente_data: IngredienteUpdate, db: Session) -> ingrediente_model:
        try:
            db_ingrediente = db.get(ingrediente_model, ingrediente_id)
            if not db_ingrediente:
                raise HTTPException(status_code=404, detail="Ingrediente not found")
            for key, value in ingrediente_data.model_dump(exclude_unset=True).items():
                setattr(db_ingrediente, key, value)
            db.add(db_ingrediente)
        except Exception as e:
            db.rollback()
            raise HTTPException(status_code=500, detail=str(e))
        finally:
            db.commit()
            db.refresh(db_ingrediente)
            return db_ingrediente

    @staticmethod
    def delete_ingrediente(ingrediente_id: int, db: Session) -> bool:
        try:
            db_ingrediente = db.get(ingrediente_model, ingrediente_id)
            if not db_ingrediente:
                raise HTTPException(status_code=404, detail="Ingrediente not found")
        except Exception as e:
            db.rollback()
            raise HTTPException(status_code=500, detail=str(e))
        finally:
            db.delete(db_ingrediente)
            db.commit()
            return True