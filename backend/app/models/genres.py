from sqlalchemy import Column, Integer, String, Date, TIMESTAMP
from backend.app.database import Base
from sqlalchemy.orm import relationship

class Genre(Base):
    __tablename__ = 'genres'
    genre_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String, nullable=False, index=True,unique=True)
