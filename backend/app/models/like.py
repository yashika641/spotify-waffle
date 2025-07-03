from sqlalchemy import Column, Integer, String, Enum, TIMESTAMP, ForeignKey, func
from sqlalchemy.orm import relationship
from backend.app.database import Base
import enum

class ItemTypeEnum(enum.Enum):
    song = 'song'
    album = 'album'
    artist = 'artist'

class Like(Base):
    __tablename__ = "likes"

    like_id = Column(Integer, primary_key=True, autoincrement=True, index=True)

    user_id = Column(Integer, ForeignKey("users.user_id", ondelete="CASCADE"), nullable=False)
    item_type = Column(Enum(ItemTypeEnum), nullable=False)
    item_id = Column(Integer, nullable=False)

    liked_at = Column(TIMESTAMP, server_default=func.now(), nullable=False)

    user = relationship("User", back_populates="likes")
