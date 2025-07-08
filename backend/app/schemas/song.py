from pydantic import BaseModel
from datetime import datetime

class SongBase(BaseModel):
    title: str
    song_url: str
    cover_url: str

class SongCreate(SongBase):
    pass

class SongResponse(SongBase):
    id: int
    uploaded_at: datetime

    class Config:
        orm_mode = True
