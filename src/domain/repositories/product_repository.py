from abc import ABC, abstractmethod
from typing import Optional
from src.domain.entities.product import Product


class ProductRepository(ABC):
    @abstractmethod
    def save(self, product: Product) -> Product: ...

    @abstractmethod
    def find_by_id(self, product_id: str) -> Optional[Product]: ...

    @abstractmethod
    def find_all(self) -> list[Product]: ...

    @abstractmethod
    def delete(self, product_id: str) -> bool: ...
