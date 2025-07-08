from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from backend.app.database import get_db
from backend.app.utils.dependencies import get_current_user
from backend.app.models.like import Like
from backend.app.models.song import Song
from backend.app.schemas.like import LikeCreate, LikeResponse

router = APIRouter(prefix="/likes", tags=["Likes"])

# ✅ Like a song
@router.post("/", response_model=LikeResponse, status_code=status.HTTP_201_CREATED)
def like_song(
    request: LikeCreate,
    db: Session = Depends(get_db),
    user: dict = Depends(get_current_user)
):
    # Validate song existence
    song = db.query(Song).filter(Song.song_id == request.song_id).first()
    if not song:
        raise HTTPException(status_code=404, detail="Song not found")

    # Check if already liked
    existing = db.query(Like).filter_by(user_id=user["sub"], song_id=request.song_id).first()
    if existing:
        raise HTTPException(status_code=400, detail="Song already liked")

    # Create like
    like = Like(user_id=user["sub"], song_id=request.song_id)
    db.add(like)
    db.commit()
    db.refresh(like)
    return like


# ✅ Unlike a song
@router.delete("/{song_id}", status_code=status.HTTP_204_NO_CONTENT)
def unlike_song(song_id: int, db: Session = Depends(get_db), user: dict = Depends(get_current_user)):
    like = db.query(Like).filter_by(user_id=user["sub"], song_id=song_id).first()
    if not like:
        raise HTTPException(status_code=404, detail="Like not found")

    db.delete(like)
    db.commit()
    return {"detail": "Song unliked"}

# ✅ Get liked songs by current user
@router.get("/", response_model=list[LikeResponse])
def get_liked_songs(db: Session = Depends(get_db), user: dict = Depends(get_current_user)):
    return db.query(Like).filter_by(user_id=user["sub"]).all()
