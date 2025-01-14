from fastapi import APIRouter, Depends, HTTPException
from typing import List
from sqlalchemy.orm import Session
from app.models.all_models import Ingrediente as ingrediente_model
from app.dto.ingrediente import IngredienteCreate, IngredienteUpdate
from app.config.database import get_db
from app.controller.ingrediente import IngredienteController

router_ingrediente = APIRouter()

@router_ingrediente.post("/", response_model=ingrediente_model)
def create_ingrediente(ingrediente_data: IngredienteCreate, db: Session = Depends(get_db)):
    return IngredienteController.create_ingrediente(ingrediente_data, db)

@router_ingrediente.get("/", response_model=List[ingrediente_model])
def list_ingredientes(db: Session = Depends(get_db)):
    return IngredienteController.list_ingredientes(db)

@router_ingrediente.get("/{ingrediente_id}", response_model=ingrediente_model)
def get_ingrediente(ingrediente_id: int, db: Session = Depends(get_db)):
    return IngredienteController.get_ingrediente(ingrediente_id, db)

@router_ingrediente.put("/{ingrediente_id}", response_model=ingrediente_model)
def update_ingrediente(ingrediente_id: int, ingrediente_data: IngredienteUpdate, db: Session = Depends(get_db)):
    return IngredienteController.update_ingrediente(ingrediente_id, ingrediente_data, db)

@router_ingrediente.delete("/{ingrediente_id}")
def delete_ingrediente(ingrediente_id: int, db: Session = Depends(get_db)):
    return {"ok": IngredienteController.delete_ingrediente(ingrediente_id, db)}

@router_ingrediente.get("/num")
def get_num_ingredientes(db: Session = Depends(get_db)):
    return IngredienteController.num_ingrediente(db)