from sqlalchemy import Column, Integer, String, DateTime, func
from backend.app.database import Base  # Adjust import path as per your setup
from sqlalchemy.orm import relationship
class Song(Base):
    __tablename__ = "songs"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255))
    song_url = Column(String(500))
    cover_url = Column(String(500))
    uploaded_at = Column(DateTime(timezone=True), server_default=func.now())
    likes = relationship("Like", back_populates="song")
    listening_history = relationship("ListeningHistory", back_populates="song", cascade="all, delete-orphan")
    playlists = relationship("PlaylistSong", back_populates="song", cascade="all, delete-orphan")
