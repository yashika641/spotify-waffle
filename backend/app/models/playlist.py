from sqlalchemy import Column, Integer, String, Date, TIMESTAMP,func ,TEXT ,BOOLEAN , ForeignKey
from backend.app.database import Base
from sqlalchemy.orm import relationship
class Playlist(Base):
    __tablename__ = 'playlists'
    
    playlist_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    title = Column(String, nullable=False, index=True)
    description = Column(TEXT, nullable=True, default=None)
    cover_image = Column(String, nullable=True, default=None)
    created_at = Column(TIMESTAMP, server_default=func.now(), nullable=False)
    is_public = Column(BOOLEAN, default=True)  # Indicates if the playlist is public or private 
    user_id = Column(
        Integer,
        ForeignKey("users.user_id", ondelete="CASCADE"),
        nullable=False
    )
    
    # Optional: Backref to get user data from playlist
    user = relationship("User", back_populates="playlists")
    songs = relationship(
    "PlaylistSong",
    back_populates="playlist",
    cascade="all, delete-orphan"
)
