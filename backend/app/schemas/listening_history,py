from pydantic import BaseModel
from datetime import datetime

class ListeningHistoryCreate(BaseModel):
    user_id: int
    song_id: int

class ListeningHistoryResponse(ListeningHistoryCreate):
    listened_at: datetime

    class Config:
        orm_mode = True
