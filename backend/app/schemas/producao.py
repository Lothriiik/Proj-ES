from pydantic import BaseModel
from typing import Optional, List
from .materiais import MaterialOut
from .sapatos import SapatoOut
from enums_definitions import StatusEnum
from .sapatos import SapatoOut
from .materiais import MaterialUsado


class ProducaoMaterialCreate(BaseModel):
    material_id: int
    quantidade_reservada: float


class ProducaoMaterialOut(BaseModel):
    id: int
    material: MaterialOut
    quantidade_reservada: float
    quantidade_usada: Optional[float] = None

    class Config:
        orm_mode = True

class ProducaoCreate(BaseModel):
    sapato_id: int
    quantidade_planejada: int
    materiais: List[ProducaoMaterialCreate]


class ProducaoOut(BaseModel):
    id: int
    sapato: SapatoOut
    quantidade_planejada: int
    quantidade_final: Optional[int]
    status: StatusEnum
    materiais: List[ProducaoMaterialOut] = []

    class Config:
        orm_mode = True


class ProducaoFinalizar(BaseModel):
    quantidade_final: float
    materiais_usados: List[MaterialUsado]

