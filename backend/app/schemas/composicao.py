from pydantic import BaseModel

class ComposicaoSapatoBase(BaseModel):
    sapato_id: int
    material_id: int

class ComposicaoSapatoCreate(ComposicaoSapatoBase):
    pass

class ComposicaoSapatoOut(ComposicaoSapatoBase):
    id: int
    sapato_id: int
    material_id: int
    sapato_nome: str  
    material_nome: str

    class Config:
        orm_mode = True


class ComposicaoSapatoCreate(BaseModel):
    sapato_id: int
    material_id: int

