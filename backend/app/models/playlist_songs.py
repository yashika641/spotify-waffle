from sqlalchemy import Column, Integer, ForeignKey, TIMESTAMP, func
from backend.app.database import Base
from sqlalchemy.orm import relationship

class PlaylistSong(Base):
    __tablename__ = 'playlist_songs'

    playlist_id = Column(
        Integer,
        ForeignKey("playlists.playlist_id", ondelete="CASCADE"),
        primary_key=True
    )

    song_id = Column(
        Integer,
        ForeignKey("songs.id", ondelete="CASCADE"),
        primary_key=True
    )

    added_at = Column(
        TIMESTAMP,
        nullable=False,
        server_default=func.now()
    )

    # Optional relationships for ORM access
    playlist = relationship("Playlist", back_populates="songs")
    song = relationship("Song", back_populates="playlists")
