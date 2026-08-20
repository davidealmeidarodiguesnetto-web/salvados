from database import engine, Base
import models  # Obrigatório para o Base registrar as classes

# Cria as tabelas no banco de dados se elas ainda não existirem
Base.metadata.create_all(bind=engine)