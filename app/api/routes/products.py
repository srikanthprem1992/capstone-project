from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.api.deps import get_db, get_current_user
from app.schemas.product import ProductCreate, ProductUpdate, ProductResponse
from app.services.product_service import *

router = APIRouter(prefix="/products", tags=["Products"])


@router.post("/", response_model=ProductResponse)
def create_product_api(
    product: ProductCreate,
    db: Session = Depends(get_db),
    user=Depends(get_current_user)
):
    return create_product_service(db, product)


@router.get("/", response_model=list[ProductResponse])
def list_products(db: Session = Depends(get_db)):
    return list_products_service(db)


@router.get("/{product_id}", response_model=ProductResponse)
def get_product(product_id: int, db: Session = Depends(get_db)):
    return get_product_service(db, product_id)


@router.put("/{product_id}", response_model=ProductResponse)
def update_product_api(
    product_id: int,
    product: ProductUpdate,
    db: Session = Depends(get_db),
    user=Depends(get_current_user)
):
    return update_product_service(db, product_id, product)


@router.delete("/{product_id}")
def delete_product_api(
    product_id: int,
    db: Session = Depends(get_db),
    user=Depends(get_current_user)
):
    return delete_product_service(db, product_id)