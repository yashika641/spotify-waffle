from sqlalchemy import column , integer , string
from database import base

class user(base):
    __tablename__ = 'users'
    id= column(integer,primary_key=True,index=True)
    username = column(string,unique=True,index=True)
    email = column(string,unique=True,index=True)
    full_name = column(string)
    bio = column(string,nullable=True)
    hashed_password = column(string)
    
    