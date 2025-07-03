from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class ArtistBase(BaseModel):
    name: str
    bio: Optional[str]
    country: Optional[str]

class ArtistCreate(ArtistBase):
    pass

class ArtistResponse(ArtistBase):
    artist_id: int
    profile_image: Optional[str]
    created_at: datetime

    class Config:
        orm_mode = True
