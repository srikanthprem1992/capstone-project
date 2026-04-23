from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.api.deps import get_db
from app.schemas.user import UserCreate, UserResponse
from app.services.user_service import register_user
from app.schemas.auth import LoginRequest, TokenResponse
from app.services.auth_service import login_user
from app.services.auth_service import change_password
from app.api.routes import auth
from app.api.deps import get_current_user
from app.schemas.auth import ChangePasswordRequest
from app.api.deps import get_current_user

router = APIRouter(prefix="/auth", tags=["Auth"])

@router.post("/register", response_model=UserResponse)
def register(user: UserCreate, db: Session = Depends(get_db)):
    return register_user(db, user)

@router.post("/login", response_model=TokenResponse)
def login(request: LoginRequest, db: Session = Depends(get_db)):
    tokens = login_user(db, request.email, request.password)
    return tokens

@router.get("/me")
def get_me(user=Depends(get_current_user)):
    return {
        "email": user.email,
        "id": user.id
    }

@router.post("/change_password")
def change_password_api(
    request: ChangePasswordRequest,
    db: Session = Depends(get_db),
    user = Depends(get_current_user)
):
    return change_password(db, user, request.old_password, request.new_password)