import uuid
from app.models.order import Order
from app.models.order_item import OrderItem
from app.models.product import Product

def create_order_service(db, user, order_data):
    total_amount = 0
    order_number = str(uuid.uuid4())

    order = Order(
        order_number=order_number,
        user_id=user.id,
        status="PLACED",
        total_amount=0
    )

    db.add(order)
    db.commit()
    db.refresh(order)

    for item in order_data.items:
        product = db.query(Product).filter(Product.id == item.product_id).first()

        if not product:
            raise Exception(f"Product {item.product_id} not found")

        if product.stock < item.quantity:
            raise Exception(f"Insufficient stock for {product.name}")

        # deduct stock
        product.stock -= item.quantity

        line_total = product.price * item.quantity
        total_amount += line_total

        order_item = OrderItem(
            order_id=order.id,
            product_id=product.id,
            sku_snapshot=product.sku,
            unit_price_snapshot=product.price,
            quantity=item.quantity,
            line_total=line_total
        )

        db.add(order_item)

    order.total_amount = total_amount

    db.commit()
    db.refresh(order)

    return order

VALID_STATUS = ["PLACED", "PAID", "SHIPPED", "DELIVERED", "CANCELLED"]

def update_order_service(db, order_id, status):
    order = db.query(Order).filter(Order.id == order_id).first()

    if not order:
        raise Exception("Order not found")

    if status not in VALID_STATUS:
        raise Exception("Invalid status")

    # Restore stock if cancelled
    if status == "CANCELLED":
        items = db.query(OrderItem).filter(OrderItem.order_id == order.id).all()

        for item in items:
            product = db.query(Product).filter(Product.id == item.product_id).first()
            product.stock += item.quantity

    order.status = status
    db.commit()
    db.refresh(order)

    return order


def delete_order_service(db, order_id):
    order = db.query(Order).filter(Order.id == order_id).first()

    if not order:
        raise Exception("Order not found")

    db.delete(order)
    db.commit()

    return {"message": "Order deleted"}