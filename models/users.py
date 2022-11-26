from sqlalchemy import(
    Column, String, Date
)

from sqlalchemy.orm import relationship 

from config.config import Base


class Users(Base):
    __tablename__ = 'users'
    id:str = Column(String, primary_key=True)
    email:str = Column(String, unique=True)
    passwd:str = Column(String)
    first_name:str = Column(String)
    last_name:str = Column(String)
    birth_date = Column(Date)
    gender:str = Column(String)
    tweets = relationship('Tweet', cascade='all, delete, delete-orphan')
    
    
    
     
    
