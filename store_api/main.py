from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import SessionLocal, engine, Base
from models import Produto
from schemas import ProdutoCreate, ProdutoResponse
import crud
from typing import List

app = FastAPI()

Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/produtos", response_model=ProdutoResponse)
def criar(produto: ProdutoCreate, db: Session = Depends(get_db)):
    return crud.criar_produto(db, produto)

@app.get("/produtos", response_model=List[ProdutoResponse])
def listar(db: Session = Depends(get_db)):
    return crud.listar_produtos(db)
