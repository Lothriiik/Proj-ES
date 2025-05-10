from sqlalchemy import Column, Integer, String, Boolean, Float, ForeignKey, DateTime, Enum as SqlEnum
from sqlalchemy.orm import relationship
from datetime import datetime
from app.db.database import Base
from app.enum import MedidaEnum, RoleEnum, StatusEnum

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    password = Column(String)
    is_active = Column(Boolean, default=True)
    role = Column(SqlEnum(RoleEnum), default="leitor")

class Material(Base):
    __tablename__ = "materials"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    description = Column(String)
    unit = Column(SqlEnum(MedidaEnum), nullable=False)

class MaterialInventory(Base):
    __tablename__ = "material_inventory"
    id = Column(Integer, primary_key=True, index=True)
    material_id = Column(Integer, ForeignKey("materials.id"))
    quantity = Column(Float, default=0.0)
    last_updated = Column(DateTime, default=datetime.utcnow)

    material = relationship("Material")

class Sapato(Base):
    __tablename__ = "sapatos"
    
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    cor = Column(String, nullable=False)
    tamanho = Column(Integer, nullable=False)

    composicoes = relationship("ComposicaoSapato", back_populates="sapato")
    producoes = relationship("Producao", back_populates="sapato")


class ComposicaoSapato(Base):
    __tablename__ = "composicao_sapato"
    id = Column(Integer, primary_key=True, index=True)
    sapato_id = Column(Integer, ForeignKey("sapatos.id"))
    material_id = Column(Integer, ForeignKey("materials.id"))

    sapato = relationship("Sapato")
    material = relationship("Material")

class Producao(Base):
    __tablename__ = "producao"
    id = Column(Integer, primary_key=True, index=True)
    sapato_id = Column(Integer, ForeignKey("sapatos.id"))
    quantidade_planejada = Column(Integer) 
    quantidade_final = Column(Integer, nullable=True)
    status = Column(SqlEnum(StatusEnum), default="planejado") 

    sapato = relationship("Sapato", back_populates="producoes")
    materiais = relationship("ProducaoMaterial", back_populates="producao")


class ProducaoMaterial(Base):
    __tablename__ = "producao_material"
    id = Column(Integer, primary_key=True, index=True)
    producao_id = Column(Integer, ForeignKey("producao.id"))
    material_id = Column(Integer, ForeignKey("materials.id"))
    quantidade_reservada = Column(Float)
    quantidade_usada = Column(Float, nullable=True)

    producao = relationship("Producao", back_populates="materiais")
    material = relationship("Material")
