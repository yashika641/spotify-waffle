from pydantic import BaseModel
from datetime import datetime
from typing import Literal

class LikeCreate(BaseModel):
    user_id: int
    item_type: Literal["song", "album", "artist"]
    item_id: int

class LikeResponse(LikeCreate):
    like_id: int
    liked_at: datetime

    class Config:
        orm_mode = True
