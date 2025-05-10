from fastapi import APIRouter, Depends, HTTPException, Body
from sqlalchemy.orm import Session
from app.db.database import get_db
from app import models
from app.schemas.usuario import UserCreate, UserOut, UserUpdate
from typing import List
from app.core.auth import get_password_hash
from app.core.auth import get_current_operador_user, get_current_admin_user


router = APIRouter()

@router.post("/criar/", response_model=UserOut, status_code=201)
def criar_usuario(

    user: UserCreate = Body(..., example={
        "username": "joaodasilva",
        "password": "senha123",
        "role": "operador"
    }, ),
    
    db: Session = Depends(get_db)
    
):
    db_user = models.User(username=user.username, password=get_password_hash(user.password), role=user.role)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

@router.get("/listar/", response_model=List[UserOut])
def listar_usuario(
    current_user: models.User = Depends(get_current_admin_user),
    db: Session = Depends(get_db)):
    return db.query(models.User).all()

@router.get("/obter/{user_id}", response_model=UserOut)
def obter_usuario(
    user_id: int, 
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_admin_user)
):
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    return user

@router.put("/atualizar/{user_id}", response_model=UserOut)
def atualizar_usuario(
    user_id: int,
    updated_user: UserUpdate = Body(..., example={
        "username": "novojonhdoe",
        "password": "novaSenha123",
        "role": "admin",
        "is_active": True
    }),
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_admin_user)
):
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    for key, value in updated_user.dict(exclude_unset=True).items():
        setattr(user, key, value)
    db.commit()
    db.refresh(user)
    return user

@router.delete("/deletar/{user_id}", status_code=204)
def deletar_usuario(
    user_id: int,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_admin_user)
):
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    db.delete(user)
    db.commit()
