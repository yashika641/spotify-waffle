from pydantic import BaseModel
from datetime import datetime

class PlaylistSongCreate(BaseModel):
    playlist_id: int
    song_id: int

class PlaylistSongResponse(PlaylistSongCreate):
    added_at: datetime

    class Config:
        orm_mode = True
