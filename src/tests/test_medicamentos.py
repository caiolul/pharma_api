def test_create_medicamento(client):
    response = client.post(
        "/medicamentos/",
        json={
            "nome": "Paracetamol",
            "descricao": "Analgésico",
            "fabricante": "Farmaceut",
            "data_validade": "2023-12-31",
            "preco": 5.99,
            "quantidade_estoque": 100,
        },
    )
    assert response.status_code == 200
    assert response.json()["nome"] == "Paracetamol"


def test_read_medicamentos(client):
    response = client.get("/medicamentos/")
    assert response.status_code == 200
    assert len(response.json()) == 1
    assert response.json()[0]["nome"] == "Paracetamol"


def test_update_medicamento(client):
    response = client.put(
        "/medicamentos/1",
        json={
            "nome": "Paracetamol",
            "descricao": "Analgésico atualizado",
            "fabricante": "Farmaceutica A",
            "data_validade": "2023-12-31",
            "preco": 6.99,
            "quantidade_estoque": 150,
        },
    )
    assert response.status_code == 200
    assert response.json()["descricao"] == "Analgésico atualizado"


def test_delete_medicamento(client):
    response = client.delete("/medicamentos/1")
    assert response.status_code == 200
    response = client.get("/medicamentos/1")
    assert response.status_code == 404
