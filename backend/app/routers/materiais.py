from fastapi import APIRouter, Depends, HTTPException, Body
from sqlalchemy.orm import Session
from app.db.database import get_db
from app import models
from app.schemas.materiais import MaterialOut, MaterialCreate, MaterialUpdate
from typing import List
from app.core.auth import get_current_operador_user, get_current_admin_user

router = APIRouter()


@router.post("/criar/", response_model=MaterialOut)
def criar_material(material: MaterialCreate, db: Session = Depends(get_db),
                   current_user: models.User = Depends(get_current_operador_user)):
    novo = models.Material(**material.dict())
    db.add(novo)
    db.commit()
    db.refresh(novo)
    return novo


@router.get("/listar/", response_model=List[MaterialOut])
def listar_materiais(db: Session = Depends(get_db),
                     current_user: models.User = Depends(get_current_operador_user)):
    return db.query(models.Material).all()

@router.get("/obter/{material_id}", response_model=MaterialOut)
def obter_material(
    material_id: int, 
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_operador_user)
):
    material = db.query(models.Material).filter(models.Material.id == material_id).first()
    if not material:
        raise HTTPException(status_code=404, detail="Material não encontrado")
    return material

@router.put("/atualizar/{material_id}", response_model=MaterialOut)
def atualizar_material(
    material_id: int,
    updated_material: MaterialUpdate = Body(..., example={
        "name": "Ferro Atualizado",
        "description": "Material metálico para construção, agora com mais estoque",
        "unit": "kg"  # 
    }),
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_operador_user)
):
    material = db.query(models.Material).filter(models.Material.id == material_id).first()
    if not material:
        raise HTTPException(status_code=404, detail="Material não encontrado")
    for key, value in updated_material.dict(exclude_unset=True).items():
        setattr(material, key, value)
    db.commit()
    db.refresh(material)
    return material

@router.delete("/deletar/{material_id}", status_code=204)
def deletar_material(
    material_id: int,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_operador_user)
):
    material = db.query(models.Material).filter(models.Material.id == material_id).first()
    if not material:
        raise HTTPException(status_code=404, detail="Material não encontrado")
    db.delete(material)
    db.commit()
