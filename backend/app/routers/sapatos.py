from fastapi import APIRouter, Depends, HTTPException, Body
from sqlalchemy.orm import Session, joinedload
from db.database import get_db
import models
from schemas.sapatos import SapatoBase, SapatoCreate, SapatoOut
from typing import List
from core.auth import get_current_operador_user, get_current_admin_user

router = APIRouter()

@router.post("/criar/", response_model=SapatoOut)
def criar_sapato(
    sapato: SapatoCreate = Body(..., example={
        "nome": "Tênis A",
        "cor": "Preto",
        "tamanho": 42,
        "composicoes": [
            {"material_id": 1},  
            {"material_id": 2}
        ]
    }),
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_operador_user)
    ):
    novo_sapato = models.Sapato(nome=sapato.nome, cor=sapato.cor, tamanho=sapato.tamanho)
    db.add(novo_sapato)
    db.commit()
    db.refresh(novo_sapato)


    for comp in sapato.composicoes:
        composicao = models.ComposicaoSapato(
            sapato_id=novo_sapato.id,
            material_id=comp.material_id
        )
        db.add(composicao)
    db.commit()

    return novo_sapato


@router.get("/listar/", response_model=List[SapatoOut])
def listar_sapatos(db: Session = Depends(get_db),
                   current_user: models.User = Depends(get_current_operador_user)):
    return db.query(models.Sapato).options(
        joinedload(models.Sapato.composicoes).joinedload(models.ComposicaoSapato.material)
    ).all()


@router.get("/obter/{sapato_id}", response_model=SapatoOut, response_description="Detalhes do sapato")
def obter_sapato(sapato_id: int, db: Session = Depends(get_db),
                 current_user: models.User = Depends(get_current_operador_user)):
    sapato = db.query(models.Sapato).options(joinedload(models.Sapato.composicoes)).filter(models.Sapato.id == sapato_id).first()
    if not sapato:
        raise HTTPException(status_code=404, detail="Sapato não encontrado")
    return sapato


@router.put("/atualizar/{sapato_id}", response_model=SapatoOut, response_description="Atualizar sapato")
def atualizar_sapato(
    sapato_id: int,
    dados: SapatoCreate = Body(
        ...,
        example={
            "nome": "Tênis A Atualizado",
            "cor": "Azul",
            "tamanho": 43,
            "composicoes": [
                {"material_id": 1},
                {"material_id": 2}
            ]
        }
    ),
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_operador_user)
):
    sapato = db.query(models.Sapato).filter(models.Sapato.id == sapato_id).first()
    if not sapato:
        raise HTTPException(status_code=404, detail="Sapato não encontrado")
    
    for key, value in dados.dict(exclude_unset=True).items():
        if key == "composicoes":
            if value:
                db.query(models.ComposicaoSapato).filter(models.ComposicaoSapato.sapato_id == sapato_id).delete()
                db.commit()

                for composicao_data in value:
                    material_id = composicao_data.get("material_id")
                    if material_id:
                        nova_composicao = models.ComposicaoSapato(
                            sapato_id=sapato_id, material_id=material_id)
                        db.add(nova_composicao)
                db.commit()
        else:
            setattr(sapato, key, value)
    
    db.commit()
    db.refresh(sapato)
    return sapato


@router.delete("/deletar/{sapato_id}", status_code=204, response_description="Deletar sapato")
def deletar_sapato(sapato_id: int, db: Session = Depends(get_db),
                   current_user: models.User = Depends(get_current_operador_user)):
    sapato = db.query(models.Sapato).filter(models.Sapato.id == sapato_id).first()
    if not sapato:
        raise HTTPException(status_code=404, detail="Sapato não encontrado")
    db.delete(sapato)
    db.commit()
