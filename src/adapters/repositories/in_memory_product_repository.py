from typing import Optional
from src.domain.entities.product import Product
from src.domain.repositories.product_repository import ProductRepository


class InMemoryProductRepository(ProductRepository):
    def __init__(self):
        self._store: dict[str, Product] = {}

    def save(self, product: Product) -> Product:
        self._store[product.id] = product
        return product

    def find_by_id(self, product_id: str) -> Optional[Product]:
        return self._store.get(product_id)

    def find_all(self) -> list[Product]:
        return list(self._store.values())

    def delete(self, product_id: str) -> bool:
        return bool(self._store.pop(product_id, None))
