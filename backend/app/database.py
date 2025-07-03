# database.py

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "mysql+pymysql://yashika:8224@localhost:3306/spotify"  # or mysql/postgresql URL

engine = create_engine(SQLALCHEMY_DATABASE_URL)  # only for SQLite

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
