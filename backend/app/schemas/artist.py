# schemas/artist_schema.py

from pydantic import BaseModel

class ArtistBase(BaseModel):
    name: str
    bio: str
    image_url: str
    country: str

class ArtistCreate(ArtistBase):
    pass

class ArtistOut(ArtistBase):
    id: int

    class Config:
        orm_mode = True
