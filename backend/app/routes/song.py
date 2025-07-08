from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from backend.app.database import get_db
from backend.app.models.song  import Song
from backend.app.schemas.song  import SongCreate, SongResponse

router = APIRouter(prefix="/songs", tags=["Songs"])

# 🔍 Get all songs
@router.get("/", response_model=list[SongResponse])
def get_all_songs(db: Session = Depends(get_db)):
    try:
        return db.query(Song).all()
    except Exception as e:
        import traceback
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=f"Server error: {str(e)}")

# 🔍 Get a song by ID
@router.get("/{song_id}", response_model=SongResponse)
def get_song(song_id: int, db: Session = Depends(get_db)):
    try:
            
        song = db.query(Song).filter(Song.id == song_id).first()
        if not song:
            raise HTTPException(status_code=404, detail="Song not found")
        return song
    except Exception as e:
        import traceback
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=f"Server error: {str(e)}")

# 🔍 Search by title
@router.get("/search/", response_model=list[SongResponse])
def search_songs(q: str, db: Session = Depends(get_db)):
    try:
            
        return db.query(Song).filter(Song.title.ilike(f"%{q}%")).all()
    except Exception as e:
        import traceback
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=f"Server error: {str(e)}")

# ➕ Add a new song
@router.post("/", response_model=SongResponse)
def create_song(song: SongCreate, db: Session = Depends(get_db)):
    try:
            
        new_song = Song(**song.dict())
        db.add(new_song)
        db.commit()
        db.refresh(new_song)
        return new_song
    except Exception as e:
        import traceback
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=f"Server error: {str(e)}")
