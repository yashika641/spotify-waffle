# routes/artist_routes.py

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from backend.app.models.artist import Artist
from backend.app.schemas.artist  import ArtistCreate, ArtistOut
from backend.app.database import get_db  # your database session dependency

router = APIRouter(
    prefix="/artists",
    tags=["Artists"]
)

@router.post("/", response_model=ArtistOut)
def create_artist(artist: ArtistCreate, db: Session = Depends(get_db)):
    try:
            
        db_artist = Artist(**artist.model_dump())
        db.add(db_artist)
        db.commit()
        db.refresh(db_artist)
        return db_artist
    except Exception as e:
        import traceback
        traceback.print_exc()  # print to console
        raise HTTPException(status_code=500, detail=f"Server error: {str(e)}")

@router.get("/", response_model=list[ArtistOut])
def get_all_artists(db: Session = Depends(get_db)):
    try:
        return db.query(Artist).all()
    except Exception as e:
        import traceback
        traceback.print_exc()  # print to console
        raise HTTPException(status_code=500, detail=f"Server error: {str(e)}")

@router.get("/{artist_id}", response_model=ArtistOut)
def get_artist(artist_id: int, db: Session = Depends(get_db)):
    try:
        artist = db.query(Artist).filter(Artist.id == artist_id).first()
        if not artist:
            raise HTTPException(status_code=404, detail="Artist not found")
        return artist

    except Exception as e:
        import traceback
        traceback.print_exc()  # print to console
        raise HTTPException(status_code=500, detail=f"Server error: {str(e)}")

    
@router.delete("/{artist_id}", response_model=dict)
def delete_artist(artist_id: int, db: Session = Depends(get_db)):
    try:
        artist = db.query(Artist).filter(Artist.id == artist_id).first()
        if not artist:
            raise HTTPException(status_code=404, detail="Artist not found")
        db.delete(artist)
        db.commit()
        return {"detail": "Artist deleted"}
    except Exception as e:
        import traceback
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=f"Server error: {str(e)}")
