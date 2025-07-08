from fastapi.security import OAuth2PasswordRequestForm
from fastapi import APIRouter, HTTPException,status, Depends
from sqlalchemy.orm import Session
from sqlalchemy import or_
from backend.app.database import get_db
from backend.app.models.user import User
from backend.app.schemas.user import UserCreate, UserResponse
from backend.app.utils.jwt_handler import create_access_token
from passlib.context import CryptContext
from backend.app.schemas.auth import LoginRequest  # 👈 You can place the schema here

router = APIRouter(prefix="/auth", tags=["Authentication"])

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_password_hash(password):
    return pwd_context.hash(password)

@router.post("/register", response_model=UserResponse)
def register_user(user: UserCreate, db: Session = Depends(get_db)):
    try:
        existing_user = db.query(User).filter(User.email == user.email).first()
        if existing_user:
            raise HTTPException(status_code=400, detail="User already exists")

        hashed_pw = get_password_hash(user.password)
        new_user = User(username=user.username, email=user.email, hashed_password=hashed_pw)
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return new_user
    except Exception as e:
        import traceback
        traceback.print_exc()  # print to console
        raise HTTPException(status_code=500, detail=f"Server error: {str(e)}")


@router.post("/login")
def login(
    login_data: LoginRequest,
    db: Session = Depends(get_db)
):
    try:
            
        user = db.query(User).filter(
            or_(User.email == login_data.username_or_email, User.username == login_data.username_or_email)
        ).first()

        if not user or not pwd_context.verify(login_data.password, user.hashed_password):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid username/email or password"
            )

        access_token = create_access_token(data={"sub": str(user.user_id)})

        return {
            "access_token": access_token,
            "token_type": "bearer"
        }
    except Exception as e:
        import traceback
        traceback.print_exc()  # print to console
        raise HTTPException(status_code=500, detail=f"Server error: {str(e)}")