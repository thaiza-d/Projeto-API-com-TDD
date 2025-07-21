from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_criar_produto():
    response = client.post("/produtos", json={
        "nome": "Camisa",
        "preco": 49.90,
        "descricao": "Camisa de algodão"
    })
    assert response.status_code == 200
    assert response.json()["nome"] == "Camisa"

def test_listar_produtos():
    response = client.get("/produtos")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
