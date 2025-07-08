from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from backend.app.database import get_db
from backend.app.models.album import Album
from backend.app.schemas.album import AlbumCreate, AlbumResponse

router = APIRouter(
    prefix="/albums",
    tags=["Albums"]
)

# CREATE album
@router.post("/", response_model=AlbumResponse, status_code=status.HTTP_201_CREATED)
def create_album(album: AlbumCreate, db: Session = Depends(get_db)):
    new_album = Album(**album.dict())
    db.add(new_album)
    db.commit()
    db.refresh(new_album)
    return new_album


# GET all albums
@router.get("/", response_model=List[AlbumResponse])
def get_all_albums(db: Session = Depends(get_db)):
    albums = db.query(Album).all()
    return albums


# GET album by ID
@router.get("/{album_id}", response_model=AlbumResponse)
def get_album_by_id(album_id: int, db: Session = Depends(get_db)):
    album = db.query(Album).filter(Album.album_id == album_id).first()
    if not album:
        raise HTTPException(status_code=404, detail="Album not found")
    return album


# UPDATE album
@router.put("/{album_id}", response_model=AlbumResponse)
def update_album(album_id: int, updated_album: AlbumCreate, db: Session = Depends(get_db)):
    album = db.query(Album).filter(Album.album_id == album_id).first()
    if not album:
        raise HTTPException(status_code=404, detail="Album not found")

    for key, value in updated_album.dict(exclude_unset=True).items():
        setattr(album, key, value)

    db.commit()
    db.refresh(album)
    return album


# DELETE album
@router.delete("/{album_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_album(album_id: int, db: Session = Depends(get_db)):
    album = db.query(Album).filter(Album.album_id == album_id).first()
    if not album:
        raise HTTPException(status_code=404, detail="Album not found")
    db.delete(album)
    db.commit()
    return {"detail": "Album deleted successfully"}
