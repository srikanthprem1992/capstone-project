from sqlalchemy.orm import Session
from app.repositories.user_repository import get_user_by_email
from app.core.security import verify_password, create_access_token, create_refresh_token
from app.core.config import ACCESS_TOKEN_EXPIRE_MINUTES, REFRESH_TOKEN_EXPIRE_MINUTES
from app.core.security import verify_password, hash_password

def login_user(db: Session, email: str, password: str):
    user = get_user_by_email(db, email)

    if not user:
        raise Exception("Invalid email or password")

    if not verify_password(password, user.password_hash):
        raise Exception("Invalid email or password")

    payload = {"sub": user.email, "user_id": user.id}

    access_token = create_access_token(payload, ACCESS_TOKEN_EXPIRE_MINUTES)
    refresh_token = create_refresh_token(payload, REFRESH_TOKEN_EXPIRE_MINUTES)

    return {
        "access_token": access_token,
        "refresh_token": refresh_token
    }


def change_password(db, user, old_password, new_password):
    # verify old password
    if not verify_password(old_password, user.password_hash):
        raise Exception("Old password is incorrect")

    # hash new password
    user.password_hash = hash_password(new_password)

    db.commit()
    db.refresh(user)

    return {"message": "Password changed successfully"}