from sqlalchemy.orm import declarative_base

Base = declarative_base()

# Import models here so metadata knows them
from app.models.user import User