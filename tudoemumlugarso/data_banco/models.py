from sqlalchemy import Column, Integer, String, Float
from database import Base

class Produto(Base):
    __tablename__ = "produtos"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(100), nullable=False)
    preco = Column(Float, nullable=False)
    estoque = Column(Integer, default=0)

class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(100), nullable=False)
    email = Column(String(150), unique=True)
    senha = Column(String(255), nullable=False)
    perfil = Column(String(20), default="comum")