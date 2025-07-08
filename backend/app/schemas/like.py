from pydantic import BaseModel
from datetime import datetime
from typing import Literal

class LikeCreate(BaseModel):
    user_id: int
    song_id: int

class LikeResponse(LikeCreate):
    like_id: int
    liked_at: datetime

    class Config:
        orm_mode = True
