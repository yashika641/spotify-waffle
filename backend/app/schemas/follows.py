from pydantic import BaseModel
from datetime import datetime

class FollowCreate(BaseModel):
    user_id: int
    artist_id: int

class FollowResponse(FollowCreate):
    followed_at: datetime

    class Config:
        orm_mode = True
