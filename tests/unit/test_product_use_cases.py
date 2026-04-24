import pytest
from src.domain.entities.product import Product
from src.adapters.repositories.in_memory_product_repository import InMemoryProductRepository
from src.use_cases.product_use_cases import ProductUseCases


@pytest.fixture
def use_cases():
    return ProductUseCases(InMemoryProductRepository())


def test_create_product(use_cases):
    p = use_cases.create("Widget", 9.99, 100)
    assert p.name == "Widget"
    assert p.id is not None


def test_get_product(use_cases):
    p = use_cases.create("Widget", 9.99, 10)
    assert use_cases.get(p.id) == p


def test_get_nonexistent_returns_none(use_cases):
    assert use_cases.get("nonexistent") is None


def test_list_all(use_cases):
    use_cases.create("A", 1.0, 1)
    use_cases.create("B", 2.0, 2)
    assert len(use_cases.list_all()) == 2


def test_delete_product(use_cases):
    p = use_cases.create("Widget", 9.99, 10)
    assert use_cases.delete(p.id) is True
    assert use_cases.get(p.id) is None


def test_invalid_price_raises():
    with pytest.raises(ValueError):
        Product(name="Bad", price=-1.0, stock=10)
