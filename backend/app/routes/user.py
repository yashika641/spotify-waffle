from fastapi import APIRouter, Depends, HTTPException, status, Header
from sqlalchemy.orm import Session
from typing import List, Optional

from backend.app.schemas.user import UserCreate, UserResponse
from backend.app.models.user import User                    
from backend.app.database import get_db
from backend.app.utils.hashing import hash_password
from backend.app.utils.jwt_handler import decode_access_token

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)

# ✅ Custom auth dependency (replaces OAuth2)
def get_current_user(authorization: Optional[str] = Header(None), db: Session = Depends(get_db)) -> User:
    if authorization is None or not authorization.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Missing or invalid token")

    token = authorization.split(" ")[1]
    payload = decode_access_token(token)
    if not payload:
        raise HTTPException(status_code=401, detail="Invalid or expired token")

    user_id = int(payload.get("sub"))
    user = db.query(User).filter(User.user_id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

# # ✅ Manual user creation (admin-side or open registration)
# @router.post('/', response_model=UserResponse)
# def create_user(user: UserCreate, db: Session = Depends(get_db)):
#     if db.query(User).filter(User.email == user.email).first():
#         raise HTTPException(status_code=400, detail='Email already registered')
#     if db.query(User).filter(User.username == user.username).first():
#         raise HTTPException(status_code=400, detail='Username already taken')
    
#     hashed_pw = hash_password(user.password)
#     db_user = User(
#         username=user.username,
#         email=user.email,
#         hashed_password=hashed_pw,
#         profile_picture=user.profile_picture,
#         country=user.country,
#         date_of_birth=user.date_of_birth,
#     )
    
#     db.add(db_user)
#     db.commit()
#     db.refresh(db_user)
#     return db_user

# ✅ Get current user profile (based on JWT)
@router.get("/me", response_model=UserResponse)
def read_my_profile(current_user: User = Depends(get_current_user)):
    return current_user

# ✅ Get user by ID
@router.get("/{user_id}", response_model=UserResponse)
def get_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.user_id == user_id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return user

# ✅ List users
@router.get('/', response_model=List[UserResponse])
def list_users(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return db.query(User).offset(skip).limit(limit).all()

# ✅ Delete user
@router.delete('/{user_id}')
def delete_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.user_id == user_id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='User not found')
    
    db.delete(user)
    db.commit()
    return {"detail": "User deleted successfully"}
