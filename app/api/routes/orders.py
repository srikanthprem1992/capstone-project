from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.api.deps import get_db, get_current_user
from app.schemas.order import OrderCreate, OrderResponse
from app.services.order_service import create_order_service
from app.schemas.order import OrderUpdate
from app.services.order_service import update_order_service
from app.services.order_service import delete_order_service

router = APIRouter(prefix="/orders", tags=["Orders"])

@router.post("/", response_model=OrderResponse)
def create_order(
    order: OrderCreate,
    db: Session = Depends(get_db),
    user = Depends(get_current_user)
):
    return create_order_service(db, user, order)

@router.put("/{order_id}")
def update_order(
    order_id: int,
    request: OrderUpdate,
    db: Session = Depends(get_db),
    user = Depends(get_current_user)
):
    return update_order_service(db, order_id, request.status)

@router.delete("/{order_id}")
def delete_order(
    order_id: int,
    db: Session = Depends(get_db),
    user = Depends(get_current_user)
):
    return delete_order_service(db, order_id)