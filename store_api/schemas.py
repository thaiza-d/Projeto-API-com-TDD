from pydantic import BaseModel

class ProdutoBase(BaseModel):
    nome: str
    preco: float
    descricao: str

class ProdutoCreate(ProdutoBase):
    pass

class ProdutoResponse(ProdutoBase):
    class Config:
        orm_mode = True
