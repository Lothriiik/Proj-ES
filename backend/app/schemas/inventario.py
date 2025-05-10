from pydantic import BaseModel
from datetime import datetime
from .materiais import MaterialOut

class InventoryCreate(BaseModel):
    material_id: int
    quantity: float

class InventoryBase(BaseModel):
    material_id: int
    quantity: float

class InventoryUpdate(InventoryBase):
    pass

class InventoryOut(InventoryBase):
    id: int
    last_updated: datetime
    material: MaterialOut
    class Config:
        orm_mode = True