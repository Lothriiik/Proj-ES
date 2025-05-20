from fastapi import APIRouter, Depends, HTTPException, Body
from sqlalchemy.orm import Session, joinedload
from db.database import get_db
import models
from schemas.sapatos import ComposicaoSapatoCreate, ComposicaoSapatoOut
from typing import List
from core.auth import get_current_operador_user, get_current_admin_user

router = APIRouter()

@router.get("/", response_model=List[ComposicaoSapatoOut])
def listar_composicoes(db: Session = Depends(get_db),
                       current_user: models.User = Depends(get_current_operador_user)):
    composicoes = db.query(models.ComposicaoSapato).options(joinedload(models.ComposicaoSapato.material)).all()
    return composicoes

@router.post("/", response_model=ComposicaoSapatoOut, status_code=201)
def criar_composicao(
    composicao: ComposicaoSapatoCreate = Body(..., example={
        "sapato_id": 1, 
        "material_id": 2 
    }),
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_operador_user)
):
    nova_composicao = models.ComposicaoSapato(**composicao.dict())
    db.add(nova_composicao)
    db.commit()
    db.refresh(nova_composicao)
    return nova_composicao

@router.get("/{composicao_id}", response_model=ComposicaoSapatoOut)
def obter_composicao(
    composicao_id: int, 
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_operador_user)
):
    composicao = db.query(models.ComposicaoSapato).options(joinedload(models.ComposicaoSapato.material)).filter(models.ComposicaoSapato.id == composicao_id).first()
    if not composicao:
        raise HTTPException(status_code=404, detail="Composição de sapato não encontrada")
    return composicao

@router.delete("/{composicao_id}", status_code=204)
def deletar_composicao(
    composicao_id: int, 
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_operador_user)
):
    composicao = db.query(models.ComposicaoSapato).filter(models.ComposicaoSapato.id == composicao_id).first()
    if not composicao:
        raise HTTPException(status_code=404, detail="Composição de sapato não encontrada")
    db.delete(composicao)
    db.commit()
