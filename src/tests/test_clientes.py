def test_create_cliente(client):
    response = client.post(
        "/cliente/",
        json={
            "nome": "Maria",
            "endereco": "Rua XPTO",
            "telefone": "83 95555-5555",
            "email": "maria.email@xpto.com",
        },
    )
    assert response.status_code == 200
    assert response.json()["nome"] == "Maria"


def test_read_medicamentos(client):
    response = client.get("/cliente/")
    assert response.status_code == 200
    assert len(response.json()) == 1
    assert response.json()[0]["nome"] == "Maria"


def test_update_medicamento(client):
    response = client.put(
        "/cliente/1",
        json={
            "nome": "Novo nome Maria",
            "endereco": "Rua XPTO",
            "telefone": "83 95555-5555",
            "email": "maria.email@xpto.com",
        },
    )
    assert response.status_code == 200
    assert response.json()["nome"] == "Novo nome Maria"


def test_delete_medicamento(client):
    response = client.delete("/cliente/1")
    assert response.status_code == 200
    response = client.get("/cliente/1")
    assert response.status_code == 404
