from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel
from src.use_cases.product_use_cases import ProductUseCases

router = APIRouter(prefix="/products", tags=["products"])


class ProductIn(BaseModel):
    name: str
    price: float
    stock: int


class ProductOut(ProductIn):
    id: str


def make_router(use_cases: ProductUseCases) -> APIRouter:
    @router.post("/", response_model=ProductOut, status_code=status.HTTP_201_CREATED)
    def create(payload: ProductIn):
        try:
            return use_cases.create(**payload.model_dump())
        except ValueError as e:
            raise HTTPException(status_code=400, detail=str(e))

    @router.get("/", response_model=list[ProductOut])
    def list_all():
        return use_cases.list_all()

    @router.get("/{product_id}", response_model=ProductOut)
    def get(product_id: str):
        product = use_cases.get(product_id)
        if not product:
            raise HTTPException(status_code=404, detail="Product not found")
        return product

    @router.delete("/{product_id}", status_code=status.HTTP_204_NO_CONTENT)
    def delete(product_id: str):
        if not use_cases.delete(product_id):
            raise HTTPException(status_code=404, detail="Product not found")

    return router
