from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker,relationship

engine = create_engine('sqlite:///sqlalchemy_example.db')
DBsession = sessionmaker(bind=engine)
session = DBsession

Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    id = Column(Integer(),primary_key=True)
    name = Column(String(20))
    articles = relationship("Article", back_populates="author")


class Article(Base):
    __tablename__ = "articles"
    id = Column(Integer(),primary_key=True)
    title = Column(String(250))
    content = Column(Text())
    user_id = Column(Integer(),ForeignKey("users.id"))
    author = relationship("User", back_populates="articles")


with engine.connect()