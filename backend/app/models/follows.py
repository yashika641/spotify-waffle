from sqlalchemy import Column , Integer , String , DATE ,TIMESTAMP ,ForeignKey, func
from backend.app.database import Base
from sqlalchemy.orm import relationship

class Follows(Base):
    __tablename__ = 'follows'
    
    user_id = Column(Integer, ForeignKey("users.user_id", ondelete="CASCADE"), nullable=False,primary_key=True)
    artist_id = Column(Integer, ForeignKey("users.user_id", ondelete="CASCADE"), nullable=False,primary_key=True)
    followed_at = Column(TIMESTAMP, nullable=False, server_default=func.now())

    # Optional: Backref to get user data from follows
    follower = relationship("User", foreign_keys=[user_id], back_populates="following")
    followed = relationship("User", foreign_keys=[artist_id], back_populates="followers") 