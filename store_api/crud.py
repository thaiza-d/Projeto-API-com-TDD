from sqlalchemy.orm import Session
from models import Produto
from schemas import ProdutoCreate

def criar_produto(db: Session, produto: ProdutoCreate):
    novo = Produto(**produto.dict())
    db.add(novo)
    db.commit()
    db.refresh(novo)
    return novo

def listar_produtos(db: Session):
    return db.query(Produto).all()
