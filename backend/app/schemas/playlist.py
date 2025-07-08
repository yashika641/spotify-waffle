from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class PlaylistBase(BaseModel):
    title: str
    description: Optional[str]
    user_id: int
    is_public: Optional[bool] = True

class PlaylistCreate(PlaylistBase):
    pass

class PlaylistResponse(PlaylistBase):
    playlist_id: int
    cover_image: Optional[str]
    created_at: datetime

    class Config:
        orm_mode = True
