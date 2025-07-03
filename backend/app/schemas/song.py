from pydantic import BaseModel
from typing import Optional

class SongBase(BaseModel):
    title: str
    duration_seconds: Optional[int]
    audio_url: str
    mood: Optional[str]
    language: Optional[str]
    album_id: Optional[int]
    artist_id: Optional[int]
    genre_id: Optional[int]

class SongCreate(SongBase):
    pass

class SongResponse(SongBase):
    song_id: int

    class Config:
        orm_mode = True
