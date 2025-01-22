from typing import List
from sqlalchemy.orm import Session
from app.models.all_models import Prato as prato_model
from app.models.all_models import PratoIngredienteLink 
from app.dto.prato import PratoCreate, PratoUpdate
from fastapi import HTTPException
from sqlmodel import select

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
    def list_pratos(db: Session) -> List[prato_model]:
        try:
            pratos = db.execute(select(prato_model)).scalars().all()
        except Exception as e:
            db.rollback()
            raise HTTPException(status_code=500, detail=str(e))
        finally:
            return pratos

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