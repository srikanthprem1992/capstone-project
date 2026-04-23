from app.models.order import Order
from app.models.order_item import OrderItem

def create_order(db, order):
    db.add(order)
    db.commit()
    db.refresh(order)
    return order

def create_order_item(db, item):
    db.add(item)
    db.commit()
    db.refresh(item)
    return item