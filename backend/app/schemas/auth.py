from pydantic import BaseModel
from typing import Optional

# 📥 When user logs infrom pydantic import BaseModel

class LoginRequest(BaseModel):
    username_or_email: str
    password: str


# 📤 What your API returns after login (JWT tokens)
class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"

# 🧠 Used internally to decode JWT
class TokenData(BaseModel):
    user_id: Optional[int] = None
    username: Optional[str] = None