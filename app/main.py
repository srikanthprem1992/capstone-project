from fastapi import FastAPI

app = FastAPI(title="Order Management System")

@app.get("/")
def root():
    return {"message": "API is running 🚀"}