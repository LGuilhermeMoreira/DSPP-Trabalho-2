from typing import Optional, Dict, Any
from sqlalchemy.orm import Session
from app.models.all_models import Prato as prato_model
from app.models.all_models import PratoIngredienteLink 
from app.dto.prato import PratoCreate, PratoUpdate
from fastapi import HTTPException
from sqlmodel import select, and_
from sqlalchemy import func
import math

class PratoController:
    @staticmethod
    def create_prato(prato_data: PratoCreate, db: Session) -> prato_model:
        try:
            db_prato = prato_model(**prato_data.model_dump())
            db.add(db_prato)
        except Exception as e:
            db.rollback()
            raise HTTPException(status_code=500, detail=str(e))
        finally:
            db.commit()
            db.refresh(db_prato)
            return db_prato

    @staticmethod
    def list_pratos(
        db: Session,
        page: int = 1,
        limit: int = 10,
        nome: Optional[str] = None,
        preco_min: Optional[float] = None,
        preco_max: Optional[float] = None,
        disponivel: Optional[bool] = None,
    ) -> Dict[str, Any]:
        try:
            offset = (page - 1) * limit
            query = select(prato_model)
            
            filters = []
            if nome:
                filters.append(prato_model.nome.ilike(f"%{nome}%"))
            if preco_min is not None:
                filters.append(prato_model.preco >= preco_min)
            if preco_max is not None:
                filters.append(prato_model.preco <= preco_max)
            if disponivel is not None:
                filters.append(prato_model.disponivel == disponivel)
                
            if filters:
                query = query.where(and_(*filters))
        
            pratos = db.execute(query.offset(offset).limit(limit)).scalars().all()
            
            total_query = select(func.count(prato_model.id))
            if filters:
                total_query = total_query.where(and_(*filters))
            
            total = db.execute(total_query).scalar()
            total_pages = math.ceil(total / limit)
            return {
                "data": pratos,
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
    def get_prato(prato_id: int, db: Session) -> prato_model:
        try:
            prato = db.get(prato_model, prato_id)
            if not prato:
                raise HTTPException(status_code=404, detail="Prato not found")
        except Exception as e:
            db.rollback()
            raise HTTPException(status_code=500, detail=str(e))
        finally:
            return prato

    @staticmethod
    def update_prato(prato_id: int, prato_data: PratoUpdate, db: Session) -> prato_model:
        try:
            db_prato = db.get(prato_model, prato_id)
            if not db_prato:
                raise HTTPException(status_code=404, detail="Prato not found")
            for key, value in prato_data.model_dump(exclude_unset=True).items():
                setattr(db_prato, key, value)
            db.add(db_prato)
        except Exception as e:
            db.rollback()
            raise HTTPException(status_code=500, detail=str(e))
        finally:
            db.commit()
            db.refresh(db_prato)
            return db_prato

    @staticmethod
    def delete_prato(prato_id: int, db: Session) -> bool:
        try:
            db_prato = db.get(prato_model, prato_id)
            if not db_prato:
                raise HTTPException(status_code=404, detail="Prato not found")
        except Exception as e:
            db.rollback()
            raise HTTPException(status_code=500, detail=str(e))
        finally:
            db.delete(db_prato)
            db.commit()
            return True
        
    @staticmethod
    def num_prato(db: Session) -> int:
        try:
            num = db.execute(select(prato_model)).count()
        except Exception as e:
            db.rollback()
            raise HTTPException(status_code=500, detail=str(e))
        finally:
            return {"quantiade" : num}
    
    #busca por texto
    @staticmethod
    def buscar_pratos_por_nome(db: Session, texto: str):
        try:
            statement = select(prato_model).where(prato_model.nome.contains(texto))
            pratos = db.exec(statement).all()
        except Exception as e:
            db.rollback()
            raise HTTPException(status_code=500, detail=str(e))
        return pratos
    
    #busca e ordenação
    @staticmethod
    def listar_pratos_ordenados_por_preco(db: Session):
        try:
            statement = select(prato_model).order_by(prato_model.preco)
            pratos = db.exec(statement).all()
        except Exception as e:
            db.rollback()
            raise HTTPException(status_code=500, detail=str(e))
        finally:
            return pratos
    
    #busca por relacionamento
    @staticmethod
    def listar_pratos_por_ingrediente(db: Session, ingrediente_id: int):
        try:
            statement = (
            select(prato_model)
            .join(PratoIngredienteLink, prato_model.id == PratoIngredienteLink.id_prato)
            .where(PratoIngredienteLink.id_ingrediente == ingrediente_id)
            )
            pratos = db.exec(statement).all()
        except Exception as e:
            db.rollback()
            raise HTTPException(status_code=500, detail=str(e))
        finally:
            return pratos