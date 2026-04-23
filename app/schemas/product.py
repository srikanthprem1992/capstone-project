from pydantic import BaseModel
from typing import Optional

class ProductCreate(BaseModel):
    sku: str
    name: str
    description: Optional[str] = None
    category: Optional[str] = None
    tags: Optional[str] = None
    price: float
    currency: str = "INR"
    stock: int = 0

class ProductUpdate(BaseModel):
    name: Optional[str]
    description: Optional[str]
    category: Optional[str]
    tags: Optional[str]
    price: Optional[float]
    stock: Optional[int]
    is_active: Optional[bool]

class ProductResponse(BaseModel):
    id: int
    sku: str
    name: str
    description: Optional[str]
    category: Optional[str]
    tags: Optional[str]
    price: float
    currency: str
    stock: int
    is_active: bool

    class Config:
        from_attributes = True