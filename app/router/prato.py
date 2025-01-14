from fastapi import APIRouter, Depends, HTTPException
from typing import List
from sqlalchemy.orm import Session
from app.models.all_models import Prato as prato_model
from app.dto.prato import PratoCreate, PratoUpdate
from app.config.database import get_db
from app.controller.prato import PratoController

router_prato = APIRouter()

@router_prato.post("/", response_model=prato_model)
def create_prato(prato_data: PratoCreate, db: Session = Depends(get_db)):
    return PratoController.create_prato(prato_data, db)

@router_prato.get("/", response_model=List[prato_model])
def list_pratos(db: Session = Depends(get_db)):
    return PratoController.list_pratos(db)

@router_prato.get("/{prato_id}", response_model=prato_model)
def get_prato(prato_id: int, db: Session = Depends(get_db)):
    return PratoController.get_prato(prato_id, db)

@router_prato.put("/{prato_id}", response_model=prato_model)
def update_prato(prato_id: int, prato_data: PratoUpdate, db: Session = Depends(get_db)):
    return PratoController.update_prato(prato_id, prato_data, db)

@router_prato.delete("/{prato_id}")
def delete_prato(prato_id: int, db: Session = Depends(get_db)):
    return {"ok": PratoController.delete_prato(prato_id, db)}