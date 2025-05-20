from fastapi import APIRouter, Depends, HTTPException, Body
from sqlalchemy.orm import Session
from db.database import get_db
import models
from schemas.inventario import InventoryOut, InventoryUpdate, InventoryCreate
from datetime import datetime
from typing import List
from core.auth import get_current_operador_user, get_current_admin_user

router = APIRouter()

@router.post("/criar/", response_model=InventoryOut, status_code=201)
def criar_inventario(
    inv: InventoryCreate = Body(..., example={
        "material_id": 1,
        "quantity": 100.0
    }),
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_operador_user)
):
    existing = db.query(models.MaterialInventory).filter(
        models.MaterialInventory.material_id == inv.material_id
    ).first()
    if existing:
        raise HTTPException(status_code=400, detail="Inventário para esse material já existe.")

    new_inventory = models.MaterialInventory(
        material_id=inv.material_id,
        quantity=inv.quantity,
        last_updated=datetime.utcnow()
    )
    db.add(new_inventory)
    db.commit()
    db.refresh(new_inventory)
    return new_inventory


@router.put("/atualizar/{material_id}", response_model=InventoryOut, status_code=200)
def atualizar_inventario(
    material_id: int, 
    inv: InventoryUpdate = Body(..., example={
        "quantity": 150.0  
    }),
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_operador_user)
):
    inventory = db.query(models.MaterialInventory).filter(models.MaterialInventory.material_id == material_id).first()
    if inventory:
        inventory.quantity = inv.quantity
        inventory.last_updated = datetime.utcnow()
    else:
        inventory = models.MaterialInventory(material_id=material_id, quantity=inv.quantity)
        db.add(inventory)
    db.commit()
    db.refresh(inventory)
    return inventory


@router.get("/listar/", response_model=List[InventoryOut])
def listar_inventario(db: Session = Depends(get_db),
                      current_user: models.User = Depends(get_current_operador_user)):
    return db.query(models.MaterialInventory).all()


@router.get("/obter/{material_id}", response_model=InventoryOut)
def obter_item_inventario(
    material_id: int, 
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_operador_user)
):
    inventory = db.query(models.MaterialInventory).filter(models.MaterialInventory.material_id == material_id).first()
    if not inventory:
        raise HTTPException(status_code=404, detail="Item de inventário não encontrado")
    return inventory


@router.delete("/deletar/{material_id}", status_code=204)
def deletar_item_inventario(
    material_id: int, 
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_operador_user)
):
    inventory = db.query(models.MaterialInventory).filter(models.MaterialInventory.material_id == material_id).first()
    if not inventory:
        raise HTTPException(status_code=404, detail="Item de inventário não encontrado")
    db.delete(inventory)
    db.commit()
