from typing import Optional
from src.domain.entities.product import Product
from src.domain.repositories.product_repository import ProductRepository


class ProductUseCases:
    def __init__(self, repo: ProductRepository):
        self._repo = repo

    def create(self, name: str, price: float, stock: int) -> Product:
        product = Product(name=name, price=price, stock=stock)
        return self._repo.save(product)

    def get(self, product_id: str) -> Optional[Product]:
        return self._repo.find_by_id(product_id)

    def list_all(self) -> list[Product]:
        return self._repo.find_all()

    def delete(self, product_id: str) -> bool:
        return self._repo.delete(product_id)
