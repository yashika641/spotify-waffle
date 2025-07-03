from sqlalchemy import Column, Integer, String , TIMESTAMP, TEXT , func
from backend.app.database import Base
from sqlalchemy.orm import relationship 

class Artist(Base):
    __tablename__ = "artists"
    artist_id = Column(Integer,autoincrement=True,primary_key=True, index=True)
    name= Column(String, nullable=False, index=True)
    bio= Column(TEXT,default=None)
    profile_image = Column(String, nullable=True, default=None)
    country = Column(String, default=None)
    created_at = Column(TIMESTAMP, server_default=func.now(), nullable=False)
    songs = relationship("Song", back_populates="artist", cascade="all, delete")
    songs = relationship("Song", back_populates="artist", cascade="all, delete-orphan")
