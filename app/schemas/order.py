from pydantic import BaseModel
from typing import List
from typing import Optional

class OrderItemCreate(BaseModel):
    product_id: int
    quantity: int

class OrderCreate(BaseModel):
    items: List[OrderItemCreate]

class OrderResponse(BaseModel):
    id: int
    order_number: str
    status: str
    total_amount: float


class OrderUpdate(BaseModel):
    status: str

class Config:
    from_attributes = True