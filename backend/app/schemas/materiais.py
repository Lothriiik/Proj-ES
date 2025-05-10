from pydantic import BaseModel
from typing import Optional
from app.enum import MedidaEnum
from datetime import datetime

class MaterialBase(BaseModel):
    name: str
    description: Optional[str]
    unit: MedidaEnum

class MaterialUsado(BaseModel):
    material_id: int
    quantidade_usada: float 


class MaterialCreate(MaterialBase):
    pass


class MaterialOut(MaterialBase):
    id: int

    class Config:
        orm_mode = True


class MaterialInventoryOut(BaseModel):
    id: int
    material_id: int
    quantity: float
    last_updated: datetime

    class Config:
        orm_mode = True

class MaterialUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    unit: Optional[MedidaEnum] = None
