from pydantic import BaseModel
from datetime import datetime

class SearchLogCreate(BaseModel):
    user_id: int
    query: str

class SearchLogResponse(SearchLogCreate):
    searched_at: datetime

    class Config:
        orm_mode = True
