from fastapi import APIRouter, Depends, HTTPException, Body
from sqlalchemy.orm import Session, joinedload
from app.db.database import get_db
from app import models
from app.enum import StatusEnum
from app.schemas.producao import ProducaoCreate, ProducaoFinalizar, ProducaoOut
from typing import List
from app.core.auth import get_current_operador_user, get_current_admin_user

router = APIRouter()


@router.post("/criar/", response_model=ProducaoOut, status_code=201)
def criar_producao(
    producao: ProducaoCreate = Body(
        ...,
        example={
            "sapato_id": 1,
            "quantidade_planejada": 100,
            "materiais": [
                {
                    "material_id": 1,
                    "quantidade_reservada": 20.0
                },
                {
                    "material_id": 2,
                    "quantidade_reservada": 15.5
                }
            ]
        }
    ),
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_operador_user)
):
    nova_producao = models.Producao(
        sapato_id=producao.sapato_id,
        quantidade_planejada=producao.quantidade_planejada,
        status="planejado"  
    )
    db.add(nova_producao)
    db.commit()
    db.refresh(nova_producao)

    for mat in producao.materiais:
        inventory = db.query(models.MaterialInventory).filter(
            models.MaterialInventory.material_id == mat.material_id
        ).first()

        if not inventory:
            raise HTTPException(status_code=404, detail=f"Inventário não encontrado para o material ID {mat.material_id}")

        if inventory.quantity < mat.quantidade_reservada:
            raise HTTPException(status_code=400, detail=f"Estoque insuficiente para o material ID {mat.material_id}")

        inventory.quantity -= mat.quantidade_reservada

        producao_material = models.ProducaoMaterial(
            producao_id=nova_producao.id,
            material_id=mat.material_id,
            quantidade_reservada=mat.quantidade_reservada
        )
        db.add(producao_material)

    db.commit()
    db.refresh(nova_producao)
    return nova_producao


@router.get("/listar/", response_model=List[ProducaoOut])
def listar_producoes(db: Session = Depends(get_db),
                     current_user: models.User = Depends(get_current_operador_user)):
    return db.query(models.Producao).options(
        joinedload(models.Producao.sapato),
        joinedload(models.Producao.materiais).joinedload(models.ProducaoMaterial.material)
    ).all()

@router.get("/obter/{producao_id}", response_model=ProducaoOut)
def obter_producao(producao_id: int, db: Session = Depends(get_db),
                   current_user: models.User = Depends(get_current_operador_user)):
    producao = db.query(models.Producao).options(
        joinedload(models.Producao.sapato),
        joinedload(models.Producao.materiais).joinedload(models.ProducaoMaterial.material)
    ).filter(models.Producao.id == producao_id).first()
    
    if not producao:
        raise HTTPException(status_code=404, detail="Produção não encontrada")
    
    return producao

@router.put("/inicar/{producao_id}/iniciar", response_model=ProducaoOut)
def iniciar_producao(
    producao_id: int,
    dados: ProducaoCreate = Body(..., example={
        "sapato_id": 2,
        "quantidade_planejada": 100,
        "materiais": [
            {"material_id": 1, "quantidade_reservada": 20},
            {"material_id": 2, "quantidade_reservada": 15.5}
        ]
    }),
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_operador_user)
):
    producao = db.query(models.Producao).filter(models.Producao.id == producao_id).first()
    if not producao:
        raise HTTPException(status_code=404, detail="Produção não encontrada")

    sapato = db.query(models.Sapato).filter(models.Sapato.id == dados.sapato_id).first()
    if sapato:
        producao.sapato = sapato
    else:
        raise HTTPException(status_code=404, detail="Sapato não encontrado")

    producao.quantidade_planejada = dados.quantidade_planejada
    producao.status = StatusEnum.em_producao

    for mat in dados.materiais:
        producao_material = db.query(models.ProducaoMaterial).filter(
            models.ProducaoMaterial.producao_id == producao_id,
            models.ProducaoMaterial.material_id == mat.material_id
        ).first()

        if producao_material:
            producao_material.quantidade_reservada = mat.quantidade_reservada
        else:
            material = db.query(models.Material).filter(models.Material.id == mat.material_id).first()
            if not material:
                raise HTTPException(status_code=404, detail=f"Material com ID {mat.material_id} não encontrado")
            
            producao_material = models.ProducaoMaterial(
                producao_id=producao.id,
                material_id=mat.material_id,
                quantidade_reservada=mat.quantidade_reservada
            )
            db.add(producao_material)

    db.commit()
    db.refresh(producao)

    return producao

@router.delete("/deletar/{producao_id}", status_code=204)
def deletar_producao(
    producao_id: int,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_operador_user)
):
    producao = db.query(models.Producao).filter(models.Producao.id == producao_id).first()
    if not producao:
        raise HTTPException(status_code=404, detail="Produção não encontrada")
    db.delete(producao)
    db.commit()

@router.put("/finalizar/{producao_id}", response_model=ProducaoOut)
def finalizar_producao(
    producao_id: int,
    producao_finalizar: ProducaoFinalizar = Body(..., example={
        "quantidade_final": 90.0,
        "materiais_usados": [
            {"material_id": 1, "quantidade_usada": 50.0},
            {"material_id": 2, "quantidade_usada": 10.0}
        ]
    }),
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_operador_user)
):
    producao = db.query(models.Producao).filter(models.Producao.id == producao_id).first()
    if not producao:
        raise HTTPException(status_code=404, detail="Produção não encontrada")

    producao.status = "finalizado"
    producao.quantidade_final = producao_finalizar.quantidade_final

    for i, mat in enumerate(producao.materiais):
        material = mat.material
        material_inventory = db.query(models.MaterialInventory).filter(
            models.MaterialInventory.material_id == material.id
        ).first()

        if not material_inventory:
            raise HTTPException(status_code=404, detail=f"Inventário do material {material.nome} não encontrado")

        quantidade_usada = producao_finalizar.materiais_usados[i].quantidade_usada
        quantidade_reservada = mat.quantidade_reservada

        diferenca = quantidade_usada - quantidade_reservada

        if diferenca > 0:
            if material_inventory.quantity < diferenca:
                raise HTTPException(status_code=400, detail=f"Estoque insuficiente para finalizar o material {material.nome}")
            material_inventory.quantity -= diferenca
        elif diferenca < 0:
            material_inventory.quantity += abs(diferenca)

        mat.quantidade_usada = quantidade_usada

    db.commit()
    db.refresh(producao)

    return producao
