from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from backend.app.database import get_db
from backend.app.models.playlist import Playlist
from backend.app.schemas.playlist import PlaylistCreate, PlaylistResponse
from backend.app.models.user import User  # Optional, for verifying ownership

router = APIRouter(
    prefix="/playlists",
    tags=["Playlists"]
)

# CREATE a playlist
@router.post("/", response_model=PlaylistResponse, status_code=status.HTTP_201_CREATED)
def create_playlist(playlist: PlaylistCreate, db: Session = Depends(get_db)):
    new_playlist = Playlist(**playlist.model_dump())
    db.add(new_playlist)
    db.commit()
    db.refresh(new_playlist)
    return new_playlist


# GET all playlists (public or admin usage)
@router.get("/", response_model=List[PlaylistResponse])
def get_all_playlists(db: Session = Depends(get_db)):
    playlists = db.query(Playlist).all()
    return playlists


# GET a single playlist by ID
@router.get("/{playlist_id}", response_model=PlaylistResponse)
def get_playlist_by_id(playlist_id: int, db: Session = Depends(get_db)):
    playlist = db.query(Playlist).filter(Playlist.playlist_id == playlist_id).first()
    if not playlist:
        raise HTTPException(status_code=404, detail="Playlist not found")
    return playlist


# DELETE a playlist
@router.delete("/{playlist_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_playlist(playlist_id: int, db: Session = Depends(get_db)):
    playlist = db.query(Playlist).filter(Playlist.playlist_id == playlist_id).first()
    if not playlist:
        raise HTTPException(status_code=404, detail="Playlist not found")
    db.delete(playlist)
    db.commit()
    return {"detail": "Playlist deleted successfully"}


# UPDATE playlist
@router.put("/{playlist_id}", response_model=PlaylistResponse)
def update_playlist(playlist_id: int, updated_data: PlaylistCreate, db: Session = Depends(get_db)):
    playlist = db.query(Playlist).filter(Playlist.playlist_id == playlist_id).first()
    if not playlist:
        raise HTTPException(status_code=404, detail="Playlist not found")

    for key, value in updated_data.dict(exclude_unset=True).items():
        setattr(playlist, key, value)

    db.commit()
    db.refresh(playlist)
    return playlist


# GET all playlists created by a specific user
@router.get("/user/{user_id}", response_model=List[PlaylistResponse])
def get_user_playlists(user_id: int, db: Session = Depends(get_db)):
    playlists = db.query(Playlist).filter(Playlist.user_id == user_id).all()
    return playlists
