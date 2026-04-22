from sqlalchemy.orm import Session
from app.repositories.user_repository import get_user_by_email, create_user
from app.core.security import hash_password

def register_user(db: Session, user):
    """Check if user already exists
        Hash password
        Prepare user object
        Call repository"""
    existing_user = get_user_by_email(db, user.email)
    if existing_user:
        raise Exception("Email already registered")

    hashed_pwd = hash_password(user.password)

    new_user = {
        "email": user.email,
        "full_name": user.full_name,
        "password_hash": hashed_pwd
    }

    return create_user(db, new_user)