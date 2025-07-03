from pydantic import BaseModel
from typing import Optional
from datetime import date

class AlbumBase(BaseModel):
    title: str
    release_date: Optional[date]
    artist_id: Optional[int]

class AlbumCreate(AlbumBase):
    pass

class AlbumResponse(AlbumBase):
    album_id: int
    cover_image: Optional[str]

    class Config:
        orm_mode = True
