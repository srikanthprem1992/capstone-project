from app.repositories.product_repository import *

def create_product_service(db, product):
    return create_product(db, product.dict())

def get_product_service(db, product_id):
    product = get_product_by_id(db, product_id)
    if not product:
        raise Exception("Product not found")
    return product

def list_products_service(db):
    return get_all_products(db)

def update_product_service(db, product_id, update_data):
    product = get_product_by_id(db, product_id)
    if not product:
        raise Exception("Product not found")

    return update_product(db, product, update_data.dict(exclude_unset=True))

def delete_product_service(db, product_id):
    product = get_product_by_id(db, product_id)
    if not product:
        raise Exception("Product not found")

    delete_product(db, product)
    return {"message": "Product deleted"}