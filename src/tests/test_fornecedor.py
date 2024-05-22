def test_create_fornecedor(client):
    response = client.post(
        "/fornecedor/",
        json={
            "nome": "Pharma Fornecedor",
            "contato": "pharma@fornecedor.com",
            "produto_fornecido": "Anti alergicos",
        },
    )
    assert response.status_code == 200
    assert response.json()["nome"] == "Pharma Fornecedor"


def test_read_fonercedor(client):
    response = client.get("/fornecedor/")
    assert response.status_code == 200
    assert len(response.json()) == 1
    assert response.json()[0]["nome"] == "Pharma Fornecedor"


def test_update_fornecedor(client):
    response = client.put(
        "/fornecedor/1",
        json={
            "nome": "Pharma Fornecedor",
            "contato": "novo_pharma@fornecedor.com",
            "produto_fornecido": "Anti alergicos",
        },
    )
    assert response.status_code == 200
    assert response.json()["contato"] == "novo_pharma@fornecedor.com"


def test_delete_fornecedor(client):
    response = client.delete("/fornecedor/1")
    assert response.status_code == 200
    response = client.get("/fornecedor/1")
    assert response.status_code == 404
