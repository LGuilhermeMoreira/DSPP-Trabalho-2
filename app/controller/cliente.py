from typing import Optional, Dict, Any
from sqlalchemy.orm import Session
from app.models.all_models import Cliente as cliente_model
from app.dto.cliente import ClienteCreate, ClienteUpdate
from fastapi import HTTPException
from sqlmodel import select, and_
from sqlalchemy import func
import math

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
    def list_clientes(
        db: Session,
        page: int = 1,
        limit: int = 10,
        nome: Optional[str] = None,
        email: Optional[str] = None,
        cpf: Optional[str] = None,
    ) -> Dict[str, Any]:
        try:
            offset = (page - 1) * limit
            query = select(cliente_model)
            
            filters = []
            if nome:
              filters.append(cliente_model.nome.ilike(f"%{nome}%"))
            if email:
               filters.append(cliente_model.email.ilike(f"%{email}%"))
            if cpf:
                filters.append(cliente_model.cpf.ilike(f"%{cpf}%"))
          
            if filters:
                query = query.where(and_(*filters))
        
            clientes = db.execute(query.offset(offset).limit(limit)).scalars().all()
            
            total_query = select(func.count(cliente_model.id))
            if filters:
                total_query = total_query.where(and_(*filters))

            total = db.execute(total_query).scalar()
            total_pages = math.ceil(total / limit)
            return {
                "data": clientes,
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
        
    @staticmethod
    def num_cliente(db: Session) -> int:
        try:
            num = db.execute(select(cliente_model)).count()
        except Exception as e:
            db.rollback()
            raise HTTPException(status_code=500, detail=str(e))
        finally:
            return {"quantiade" : num}