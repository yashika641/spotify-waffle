from sqlalchemy import Column , Integer , String ,TIMESTAMP,ForeignKey,func 
from backend.app.database import Base
from sqlalchemy.orm import relationship

class SearchLog(Base):
    __tablename__ = 'search_logs'
    id= Column(Integer, primary_key=True, autoincrement=True, index=True)
    query = Column(String, nullable=False)
    searched_at = Column(TIMESTAMP, nullable=False,server_default= func.now())
    
    user_id = Column(
        Integer,
        ForeignKey("users.user_id", ondelete="CASCADE"),
        nullable=False
    )
    # Optional: Backref to get user data from search log
    user = relationship("User", back_populates="search_logs")