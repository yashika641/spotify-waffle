# models/artist_model.py

from sqlalchemy import Column, Integer, String, Text
from backend.app.database import Base  # assuming database.py defines `Base = declarative_base()`
from sqlalchemy.orm import relationship
class Artist(Base):
    __tablename__ = "artist"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    bio = Column(Text)
    image_url = Column(Text)
    country = Column(String(100))
    albums = relationship("Album", back_populates="artist", cascade="all, delete-orphan")
    followers = relationship("Follows", back_populates="followed", cascade="all, delete-orphan")
