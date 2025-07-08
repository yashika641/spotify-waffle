from sqlalchemy import Column, Integer, TIMESTAMP, ForeignKey, func
from sqlalchemy.orm import relationship
from backend.app.database import Base

class ListeningHistory(Base):
    __tablename__ = 'listening_history'

    user_id = Column(
        Integer,
        ForeignKey("users.user_id", ondelete="CASCADE"),
        primary_key=True
    )

    song_id = Column(
        Integer,
        ForeignKey("songs.id", ondelete="CASCADE"),
        primary_key=True
    )

    listened_at = Column(
        TIMESTAMP,
        server_default=func.now(),
        nullable=False
    )

    # Optional relationships
    user = relationship("User", back_populates="listening_history")
    song = relationship("Song", back_populates="listening_history")
