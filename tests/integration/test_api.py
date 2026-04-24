import pytest
from fastapi.testclient import TestClient
from src.infrastructure.config.app import app

client = TestClient(app)


def test_health():
    assert client.get("/health").status_code == 200


def test_create_and_get_product():
    res = client.post("/products/", json={"name": "Gadget", "price": 19.99, "stock": 5})
    assert res.status_code == 201
    product_id = res.json()["id"]

    res = client.get(f"/products/{product_id}")
    assert res.status_code == 200
    assert res.json()["name"] == "Gadget"


def test_list_products():
    res = client.get("/products/")
    assert res.status_code == 200
    assert isinstance(res.json(), list)


def test_delete_product():
    res = client.post("/products/", json={"name": "ToDelete", "price": 1.0, "stock": 1})
    product_id = res.json()["id"]
    assert client.delete(f"/products/{product_id}").status_code == 204


def test_get_nonexistent_returns_404():
    assert client.get("/products/nonexistent").status_code == 404
