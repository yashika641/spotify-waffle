from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class UserBase(BaseModel):
    username: str
    email: EmailStr
    full_name: Optional[str] = None
    bio: Optional[str] = None
    
class userout(UserBase):
    id: int
    
    class Config:
        orm_mode = True
        
class userupdate(BaseModel):
    full_name: Optional[str]= Field(None)
    bio: Optional[str]= Field(None)