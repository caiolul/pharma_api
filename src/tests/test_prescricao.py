def test_create_prescricao(client):
    response = client.post(
        "/prescricao/",
        json={
            "cliente_id": 1,
            "medicamento_id": 1,
            "quantidade": 50,
            "data_prescricao": "2024-05-11",
        },
    )
    assert response.status_code == 200
    assert response.json()["data_prescricao"] == "2024-05-11"


def test_read_prescricao(client):
    response = client.get("/prescricao/")
    assert response.status_code == 200
    assert len(response.json()) == 1
    assert response.json()[0]["cliente_id"] == 1
    assert response.json()[0]["medicamento_id"] == 1


def test_update_prescricao(client):
    response = client.put(
        "/prescricao/1",
        json={
            "cliente_id": 1,
            "medicamento_id": 1,
            "quantidade": 100,
            "data_prescricao": "2024-05-16",
        },
    )
    assert response.status_code == 200
    assert response.json()["data_prescricao"] == "2024-05-16"


def test_delete_prescricao(client):
    response = client.delete("/prescricao/1")
    assert response.status_code == 200
    response = client.get("/prescricao/1")
    assert response.status_code == 404
