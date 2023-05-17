from sqlalchemy.engine import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base, relationship


engine = create_engine("sqlite:///college.db")
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()
