from fastapi import APIRouter, Depends, HTTPException
from typing import List
from sqlalchemy.orm import Session
from app.models.all_models import Comanda as comanda_model
from app.dto.comanda import ComandaCreate, ComandaUpdate
from app.config.database import get_db
from app.controller.comanda import ComandaController

router_comanda = APIRouter()

@router_comanda.post("/", response_model=comanda_model)
def create_comanda(comanda_data: ComandaCreate, db: Session = Depends(get_db)):
    return ComandaController.create_comanda(comanda_data, db)

@router_comanda.get("/", response_model=List[comanda_model])
def list_comandas(db: Session = Depends(get_db)):
    return ComandaController.list_comandas(db)

@router_comanda.get("/{comanda_id}", response_model=comanda_model)
def get_comanda(comanda_id: int, db: Session = Depends(get_db)):
    return ComandaController.get_comanda(comanda_id, db)

@router_comanda.put("/{comanda_id}", response_model=comanda_model)
def update_comanda(comanda_id: int, comanda_data: ComandaUpdate, db: Session = Depends(get_db)):
    return ComandaController.update_comanda(comanda_id, comanda_data, db)

@router_comanda.delete("/{comanda_id}")
def delete_comanda(comanda_id: int, db: Session = Depends(get_db)):
    return {"ok": ComandaController.delete_comanda(comanda_id, db)}