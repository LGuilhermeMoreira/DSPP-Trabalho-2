from fastapi import APIRouter, Depends, HTTPException
from typing import List
from sqlalchemy.orm import Session
from app.models.all_models import Mesa as mesa_model
from app.dto.mesa import MesaCreate, MesaUpdate
from app.config.database import get_db
from app.controller.mesa import MesaController

router_mesa = APIRouter()

@router_mesa.post("/", response_model=mesa_model)
def create_mesa(mesa_data: MesaCreate, db: Session = Depends(get_db)):
    return MesaController.create_mesa(mesa_data, db)

@router_mesa.get("/", response_model=List[mesa_model])
def list_mesas(db: Session = Depends(get_db)):
    return MesaController.list_mesas(db)

@router_mesa.get("/{mesa_id}", response_model=mesa_model)
def get_mesa(mesa_id: int, db: Session = Depends(get_db)):
    return MesaController.get_mesa(mesa_id, db)

@router_mesa.put("/{mesa_id}", response_model=mesa_model)
def update_mesa(mesa_id: int, mesa_data: MesaUpdate, db: Session = Depends(get_db)):
    return MesaController.update_mesa(mesa_id, mesa_data, db)

@router_mesa.delete("/{mesa_id}")
def delete_mesa(mesa_id: int, db: Session = Depends(get_db)):
    return {"ok": MesaController.delete_mesa(mesa_id, db)}

@router_mesa.get("/num")
def get_num_mesas(db: Session = Depends(get_db)):
    return MesaController.um_mesa(db)