from sqlalchemy import Column , Integer , String , DATE ,TIMESTAMP
from backend.app.database import Base
from sqlalchemy.orm import relationship
class User(Base):
    __tablename__ = 'users'
    user_id= Column(Integer,primary_key=True,index=True,autoincrement=True)
    username = Column(String,unique=True,index=True,nullable=False)
    email = Column(String,unique=True,index=True,nullable=False)
    hashed_password = Column(String,nullable=False)
    profile_picture = Column(String,nullable=True,default=None)
    country = Column(String,default=None)
    created_at = Column(TIMESTAMP,default=None)
    date_of_birth = Column(DATE,default=None)
    
    
    # Optional: Backref to get user data from playlist
    playlists = relationship("Playlist", back_populates="user", cascade="all, delete")
    following = relationship("Follows", foreign_keys="Follows.user_id", back_populates="follower", cascade="all, delete")
    followers = relationship("Follows", foreign_keys="Follows.artist_id", back_populates="followed", cascade="all, delete")
    search_logs = relationship("SearchLog", back_populates="user", cascade="all, delete")
    likes = relationship("Like", back_populates="user", cascade="all, delete-orphan")
    listening_history = relationship(
    "ListeningHistory", back_populates="user", cascade="all, delete-orphan"
)
