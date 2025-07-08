from sqlalchemy import Column, Integer, Enum, TIMESTAMP, ForeignKey, func
from sqlalchemy.orm import relationship
from backend.app.database import Base
import enum

class ItemTypeEnum(enum.Enum):
    song = 'song'
    album = 'album'
    artist = 'artist'

class Like(Base):
    __tablename__ = "likes"

    id = Column(Integer, primary_key=True)
    song_id = Column(Integer, ForeignKey('songs.id'))  # ✅ Now SQLAlchemy knows how to join

    song = relationship("Song", back_populates="likes")