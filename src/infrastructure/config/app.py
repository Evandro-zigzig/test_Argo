from fastapi import FastAPI
from src.adapters.api.product_router import make_router
from src.adapters.repositories.in_memory_product_repository import InMemoryProductRepository
from src.use_cases.product_use_cases import ProductUseCases

app = FastAPI(title="Clean Architecture API", version="1.0.0")

repo = InMemoryProductRepository()
use_cases = ProductUseCases(repo)
app.include_router(make_router(use_cases))


@app.get("/health")
def health():
    return {"status": "ok"}
