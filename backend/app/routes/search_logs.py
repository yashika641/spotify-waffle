from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from backend.app.database import get_db
from backend.app.utils.dependencies import get_current_user
from backend.app.models.search_logs import SearchLog
from backend.app.schemas.search_log import SearchLogCreate, SearchLogResponse
from typing import List

router = APIRouter(prefix="/search", tags=["Search"])

@router.post("/log", response_model=SearchLogResponse)
def log_search(query: SearchLogCreate, db: Session = Depends(get_db), user: dict = Depends(get_current_user)):
    log = SearchLog(user_id=user["sub"], query=query.query)
    db.add(log)
    db.commit()
    db.refresh(log)
    return log

@router.get("/history", response_model=List[SearchLogResponse])
def get_search_history(db: Session = Depends(get_db), user: dict = Depends(get_current_user)):
    return db.query(SearchLog).filter_by(user_id=user["sub"]).order_by(SearchLog.timestamp.desc()).all()
