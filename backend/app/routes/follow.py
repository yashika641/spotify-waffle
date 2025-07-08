from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from backend.app.database import get_db
from backend.app.utils.dependencies import get_current_user
from backend.app.models.follows import Follows 
from backend.app.models.artist import Artist
from backend.app.schemas.follows import FollowCreate, FollowResponse
from typing import List

router = APIRouter(prefix="/follow", tags=["Follow"])

@router.post("/artist", response_model=FollowResponse)
def follow_artist(data: FollowCreate, db: Session = Depends(get_db), user: dict = Depends(get_current_user)):
    # ✅ Optional: Validate artist exists
    artist = db.query(Artist).filter(Artist.artist_id == data.artist_id).first()
    if not artist:
        raise HTTPException(status_code=404, detail="Artist not found")

    existing = db.query(Follows).filter_by(user_id=user["sub"], artist_id=data.artist_id).first()
    if existing:
        raise HTTPException(status_code=400, detail="Already following this artist")

    follow = Follows(user_id=user["sub"], artist_id=data.artist_id)
    db.add(follow)
    db.commit()
    db.refresh(follow)
    return follow


@router.delete("/artist/{artist_id}")
def unfollow_artist(artist_id: int, db: Session = Depends(get_db), user: dict = Depends(get_current_user)):
    follow = db.query(Follows).filter_by(user_id=user["sub"], artist_id=artist_id).first()
    if not follow:
        raise HTTPException(status_code=404, detail="Follow not found")
    db.delete(follow)
    db.commit()
    return {"detail": "Unfollowed artist"}

@router.get("/artists", response_model=List[FollowResponse])
def get_followed_artists(db: Session = Depends(get_db), user: dict = Depends(get_current_user)):
    return db.query(Follows).filter_by(user_id=user["sub"]).all()
