from sqlalchemy import Column , Integer , String , DATE ,TIMESTAMP,ForeignKey
from backend.app.database import Base
from sqlalchemy.orm import relationship

class Song(Base):
    __tablename__ = "songs"

    song_id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    title = Column(String(150), nullable=False)
    duration_seconds = Column(Integer, nullable=True)
    audio_url = Column(String(255), nullable=False)

    mood = Column(String(50), nullable=True)
    language = Column(String(50), nullable=True)

    album_id = Column(
        Integer,
        ForeignKey("albums.album_id", ondelete="SET NULL"),
        nullable=True
    )

    artist_id = Column(
        Integer,
        ForeignKey("artists.artist_id", ondelete="SET NULL"),
        nullable=True
    )

    genre_id = Column(
        Integer,
        ForeignKey("genres.genre_id", ondelete="SET NULL"),
        nullable=True
    )

    # Optional relationships
    album = relationship("Album", back_populates="songs")
    artist = relationship("Artist", back_populates="songs")
    genre = relationship("Genre", back_populates="songs")


    listening_history = relationship(
        "ListeningHistory", back_populates="user", cascade="all, delete-orphan"
    )
    playlists = relationship(
        "PlaylistSong",
        back_populates="song",
        cascade="all, delete-orphan"
    )
