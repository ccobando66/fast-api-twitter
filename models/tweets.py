from datetime import datetime

from sqlalchemy import(
    Column, String, DateTime, ForeignKey
)

from config.config import Base

class Tweet(Base):
    __tablename__ = 'tweets'
    id:str = Column(String, primary_key=True)
    content:str = Column(String)
    created_at = Column(DateTime)
    update_at = Column(DateTime)
    users = Column(String, ForeignKey('users.id'))
    
    
    