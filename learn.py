from sqlalchemy.engine import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base, relationship
from sqlalchemy import Column, String, Integer, Text,ForeignKey


engine = create_engine("sqlite:///test.db")

Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()


class User(Base):
    __tablename__ = "users"
    id = Column(Integer(),primary_key=True)
    name = Column(String(30))
    articles = relationship("Articles", back_populates="author")

class Articles(Base):
    __tablename__ = "articles"
    id = Column(Integer(), primary_key=True)
    title = Column(String(250))
    content = Column(Text())
    user_id = Column(Integer(), ForeignKey("users.id"))
    author = relationship("User",back_populates="articles")

Base.metadata.create_all(engine)
Base.metadata.bind = engine

