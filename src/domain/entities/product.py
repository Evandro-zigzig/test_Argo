from dataclasses import dataclass, field
from uuid import uuid4


@dataclass
class Product:
    name: str
    price: float
    stock: int
    id: str = field(default_factory=lambda: str(uuid4()))

    def __post_init__(self):
        if self.price < 0:
            raise ValueError("Price cannot be negative")
        if self.stock < 0:
            raise ValueError("Stock cannot be negative")
