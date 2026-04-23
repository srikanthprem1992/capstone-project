from sqlalchemy.orm import declarative_base

Base = declarative_base()

# Import models here so metadata knows them
from app.models.user import User
from app.models.product import Product
from app.models.order import Order
from app.models.order_item import OrderItem