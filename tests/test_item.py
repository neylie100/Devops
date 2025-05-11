from fastapi.testclient import TestClient


from main import app


client = TestClient(app)


def test_create():
    response = client.post(
        "/items",
        json={"name": "Test1", "price": 10.99, "in_stock": True},
    )
    assert response.status_code == 200
    assert response.json()["success"] is True
    assert "message" in response.json()


def test_read_items():
    response = client.get("/items")
    assert response.status_code == 200
    assert response.json()["success"] is True
    assert isinstance(response.json()["data"], list)


def test_read_only_item():
    client.post(
        "/items",
        json={"name": "SingleItem", "price": 15.0, "in_stock": False},
    )

    response_all = client.get("/items")
    last_item = response_all.json()["data"][-1]
    item_id = last_item["id"]

    response = client.get(f"/items/{item_id}")
    assert response.status_code == 200
    assert response.json()["success"] is True
    assert response.json()["data"]["id"] == item_id


def test_update():

    client.post(
        "/items",
        json={"name": "UpdateMe", "price": 25.0, "in_stock": True},
    )
    response_all = client.get("/items")
    item_id = response_all.json()["data"][-1]["id"]

    response = client.put(
        f"/items/{item_id}",
        json={"name": "Updated", "price": 26.0, "in_stock": False},
    )
    assert response.status_code == 200
    assert response.json()["success"] is True
    assert response.json()["message"] == "Item mis à jour avec succès"


def test_delete():

    client.post(
        "/items",
        json={"name": "Delete", "price": 5.0, "in_stock": False},
    )
    response_all = client.get("/items")
    item_id = response_all.json()["data"][-1]["id"]

    response = client.delete(f"/items/{item_id}")
    assert response.status_code == 200
    assert response.json()["success"] is True
    assert response.json()["message"] == "Item supprimé avec succès"

    response = client.get(f"/items/{item_id}")
    assert response.status_code == 200
    assert response.json()["success"] is False
