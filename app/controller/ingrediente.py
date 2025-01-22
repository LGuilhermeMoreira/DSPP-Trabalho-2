from typing import List, Optional, Dict, Any
from sqlalchemy.orm import Session
from app.models.all_models import Ingrediente as ingrediente_model
from app.dto.ingrediente import IngredienteCreate, IngredienteUpdate
from fastapi import HTTPException
from sqlmodel import select, and_
from sqlalchemy import func
import math

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
    def list_ingredientes(
        db: Session,
        page: int = 1,
        limit: int = 10,
        nome: Optional[str] = None,
        estoque: Optional[bool] = None,
        quantidade_estoque_min: Optional[float] = None,
        quantidade_estoque_max: Optional[float] = None,
        peso: Optional[float] = None,
    ) -> Dict[str, Any]:
        try:
            offset = (page - 1) * limit
            query = select(ingrediente_model)
            
            filters = []
            if nome:
                filters.append(ingrediente_model.nome.ilike(f"%{nome}%"))
            if estoque is not None:
                filters.append(ingrediente_model.estoque == estoque)
            if quantidade_estoque_min is not None:
                filters.append(ingrediente_model.quantidade_estoque >= quantidade_estoque_min)
            if quantidade_estoque_max is not None:
                filters.append(ingrediente_model.quantidade_estoque <= quantidade_estoque_max)
            if peso is not None:
                filters.append(ingrediente_model.peso == peso)

            if filters:
                query = query.where(and_(*filters))
        
            ingredientes = db.execute(query.offset(offset).limit(limit)).scalars().all()
            
            total_query = select(func.count(ingrediente_model.id))
            if filters:
                total_query = total_query.where(and_(*filters))
            
            total = db.execute(total_query).scalar()
            total_pages = math.ceil(total / limit)
            return {
                "data": ingredientes,
                "pagination": {
                    "total": total,
                    "currentPage": page,
                    "totalPages": total_pages,
                    "totalItemsPerPage": limit
                },
            }
        except Exception as e:
            db.rollback()
            raise HTTPException(status_code=500, detail=str(e))

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
    
    @staticmethod
    def num_ingrediente(db: Session) -> int:
        try:
            num = db.execute(select(ingrediente_model)).count()
        except Exception as e:
            db.rollback()
            raise HTTPException(status_code=500, detail=str(e))
        finally:
            return {"quantiade" : num}
    
    