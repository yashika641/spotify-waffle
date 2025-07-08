from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from backend.app.database import get_db
from backend.app.utils.dependencies import get_current_user
from backend.app.models.listening_history import ListeningHistory
from backend.app.schemas.listening_history import ListeningHistoryCreate,ListeningHistoryResponse
from typing import List

router = APIRouter(prefix="/history", tags=["Listening History"])

@router.post("/", response_model=ListeningHistoryResponse)
def add_to_history(entry: ListeningHistoryCreate, db: Session = Depends(get_db), user: dict = Depends(get_current_user)):
    log = ListeningHistory(user_id=user["sub"], song_id=entry.song_id)
    db.add(log)
    db.commit()
    db.refresh(log)
    return log

@router.get("/", response_model=List[ListeningHistoryResponse])
def get_listening_history(db: Session = Depends(get_db), user: dict = Depends(get_current_user)):
    return db.query(ListeningHistory).filter_by(user_id=user["sub"]).order_by(ListeningHistory.listened_at.desc()).all()
