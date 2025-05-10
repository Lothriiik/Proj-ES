from pydantic import BaseModel
from typing import List, Optional
from .materiais import MaterialOut


class ComposicaoSapatoCreate(BaseModel):
    material_id: int


class ComposicaoSapatoOut(BaseModel):
    id: int
    material: MaterialOut

    class Config:
        orm_mode = True


class SapatoBase(BaseModel):
    nome: str
    cor: str
    tamanho: int


class SapatoCreate(SapatoBase):
    composicoes: List[ComposicaoSapatoCreate] = []


class SapatoOut(SapatoBase):
    id: int
    composicoes: List[ComposicaoSapatoOut] = []

    class Config:
        orm_mode = True
