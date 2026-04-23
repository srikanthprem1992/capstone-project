from fastapi import FastAPI
from app.db.base import Base
from app.db.session import engine
from app.api.routes import auth
from app.api.routes import products
from app.api.routes import orders
from app.core.middleware import logging_middleware

# app.db file creation
Base.metadata.create_all(bind=engine)

#fast api 
app = FastAPI(title="Order Management System")

@app.get("/")
def root():
    return {"message": "API is running 🚀"}

app.include_router(auth.router)
app.include_router(products.router)
app.include_router(orders.router)
app.middleware("http")(logging_middleware)
