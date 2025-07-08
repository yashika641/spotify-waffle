from sqlalchemy import Column , Integer , String , DATE ,TIMESTAMP,func
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
    created_at = Column(TIMESTAMP, server_default=func.now(), nullable=False)
    date_of_birth = Column(DATE,default=None,nullable=True)
    
    
    # Optional: Backref to get user data from playlist
    playlists = relationship("Playlist", back_populates="user", cascade="all, delete")
    following = relationship("Follows", back_populates="follower", cascade="all, delete")
    search_logs = relationship("SearchLog", back_populates="user", cascade="all, delete")
    listening_history = relationship(
    "ListeningHistory", back_populates="user", cascade="all, delete-orphan"
)
