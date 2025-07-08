from sqlalchemy import Column, Integer, String, Date, ForeignKey 
from backend.app.database import Base
from sqlalchemy.orm import relationship

class Album(Base):
    __tablename__ = 'albums'
    
    album_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    title = Column(String, nullable=False, index=True)
    
    artist_id = Column(
        Integer,
        ForeignKey("artist.id", ondelete="CASCADE"),
        nullable=False
    )

    release_date = Column(Date, nullable=True)
    cover_image = Column(String, nullable=True, default=None)

    # Only this relationship remains
    artist = relationship("Artist", back_populates="albums")
