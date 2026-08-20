from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import engine, Base, get_db
import models

# PASSO 2 DO SLIDE: Gera as tabelas 'produtos' e 'usuarios' no SQL Server automaticamente
Base.metadata.create_all(bind=engine)

app = FastAPI()

# PASSO 4 DO SLIDE: Rota de teste que insere um produto via ORM
@app.post("/teste-produto")
def criar_produto_teste(db: Session = Depends(get_db)):
    # Criamos o objeto Python do produto
    novo_produto = models.Produto(
        nome="Teclado Gamer",
        preco=250.00,
        estoque=15
    )
    
    # O ORM salva no SQL Server
    db.add(novo_produto)
    db.commit()
    db.refresh(novo_produto)
    
    return {"mensagem": "Produto inserido com sucesso!", "produto": novo_produto}