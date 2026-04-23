from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException
from jose import jwt, JWTError
from app.db.session import SessionLocal
from app.core.config import SECRET_KEY, ALGORITHM
from app.models.user import User
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials


# existing DB dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


security = HTTPBearer()

def get_token(credentials: HTTPAuthorizationCredentials = Depends(security)):
    return credentials.credentials

def get_current_user(
    db: Session = Depends(get_db),
    token: str = Depends(get_token)
):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id = payload.get("user_id")

        if user_id is None:
            raise HTTPException(status_code=401, detail="Invalid token")

        user = db.query(User).filter(User.id == user_id).first()

        if user is None:
            raise HTTPException(status_code=401, detail="User not found")

        return user

    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid or expired token")