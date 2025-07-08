from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from backend.app.database import get_db
from backend.app.models.genres import genres as Genre
from backend.app.schemas.genres import GenreCreate, GenreResponse

router = APIRouter(
    prefix="/genres",
    tags=["Genres"]
)

# ✅ Create a genre
@router.post("/", response_model=GenreResponse, status_code=status.HTTP_201_CREATED)
def create_genre(genre: GenreCreate, db: Session = Depends(get_db)):
    existing = db.query(Genre).filter(Genre.name == genre.name).first()
    if existing:
        raise HTTPException(status_code=400, detail="Genre already exists")
    
    new_genre = Genre(name=genre.name)
    db.add(new_genre)
    db.commit()
    db.refresh(new_genre)
    return new_genre


# ✅ Get all genres
@router.get("/", response_model=List[GenreResponse])
def get_all_genres(db: Session = Depends(get_db)):
    return db.query(Genre).all()


# ✅ Get a single genre by ID
@router.get("/{genre_id}", response_model=GenreResponse)
def get_genre_by_id(genre_id: int, db: Session = Depends(get_db)):
    genre = db.query(Genre).filter(Genre.genre_id == genre_id).first()
    if not genre:
        raise HTTPException(status_code=404, detail="Genre not found")
    return genre


# ✅ Update a genre
@router.put("/{genre_id}", response_model=GenreResponse)
def update_genre(genre_id: int, updated_data: GenreCreate, db: Session = Depends(get_db)):
    genre = db.query(Genre).filter(Genre.genre_id == genre_id).first()
    if not genre:
        raise HTTPException(status_code=404, detail="Genre not found")
    
    genre.name = updated_data.name
    db.commit()
    db.refresh(genre)
    return genre


# ✅ Delete a genre
@router.delete("/{genre_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_genre(genre_id: int, db: Session = Depends(get_db)):
    genre = db.query(Genre).filter(Genre.genre_id == genre_id).first()
    if not genre:
        raise HTTPException(status_code=404, detail="Genre not found")
    
    db.delete(genre)
    db.commit()
    return {"detail": "Genre deleted successfully"}
