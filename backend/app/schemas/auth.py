from pydantic import BaseModel, EmailStr
from typing import Optional

# 📥 When user logs in
class LoginRequest(BaseModel):
    email: EmailStr
    password: str

# 📤 What your API returns after login (JWT tokens)
class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"

# 🧠 Used internally to decode JWT
class TokenData(BaseModel):
    user_id: Optional[int] = None
    username: Optional[str] = None