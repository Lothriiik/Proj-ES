from pydantic import BaseModel
from typing import Optional
from app.enum import RoleEnum 

class UserBase(BaseModel):
    username: str
    role: Optional[RoleEnum] = RoleEnum.leitor 

class UserCreate(UserBase):
    password: str

class UserUpdate(BaseModel):
    username: Optional[str] = None
    password: Optional[str] = None
    role: Optional[RoleEnum] = None 
    is_active: Optional[bool] = None

class UserOut(UserBase):
    id: int
    is_active: bool

    class Config:
        orm_mode = True
