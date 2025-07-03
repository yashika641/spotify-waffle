from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import date, datetime

class UserBase(BaseModel):
    username: str
    email: EmailStr
    country: Optional[str]
    date_of_birth: Optional[date]

class UserCreate(UserBase):
    password: str

class UserResponse(UserBase):
    user_id: int
    profile_picture: Optional[str]
    created_at: datetime

    class Config:
        orm_mode = True
