from fastapi import FastAPI
from app.db.base import Base
from app.db.session import engine

# app.db file creation
Base.metadata.create_all(bind=engine)

#fast api 
app = FastAPI(title="Order Management System")

@app.get("/")
def root():
    return {"message": "API is running 🚀"}