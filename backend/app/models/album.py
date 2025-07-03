from sqlalchemy import Column, Integer, String, Date, ForeignKey 
from backend.app.database import Base
from sqlalchemy.orm import relationship

class Album(Base):
    __tablename__ = 'albums'
    
    album_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    title = Column(String, nullable=False, index=True)
    artist_id = Column(Integer, nullable=False)  # Assuming a foreign key relationship with Artist
    release_date = Column(Date, nullable=True)
    cover_image = Column(String, nullable=True, default=None)
    artist_id = Column(
        Integer,
        ForeignKey("artists.artist_id", ondelete="CASCADE"),
        nullable=False
    )

    # Optional: Backref to get artist data from song
    artist = relationship("Artist", back_populates="songs")
    
    songs = relationship("Song", back_populates="album", cascade="all, delete-orphan")
