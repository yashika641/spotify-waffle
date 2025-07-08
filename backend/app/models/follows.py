from sqlalchemy import Column, Integer, TIMESTAMP, ForeignKey, func
from sqlalchemy.orm import relationship
from backend.app.database import Base

class Follows(Base):
    __tablename__ = 'follows'
    
    user_id = Column(
        Integer,
        ForeignKey("users.user_id", ondelete="CASCADE"),
        primary_key=True
    )

    artist_id = Column(
        Integer,
        ForeignKey("artist.id", ondelete="CASCADE"),  # FIXED
        primary_key=True
    )

    followed_at = Column(TIMESTAMP, nullable=False, server_default=func.now())

    # Relationships
    follower = relationship("User", back_populates="following")
    followed = relationship("Artist", back_populates="followers")  # FIXED
