from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase


db = create_engine('sqlite:///./database.db')

class Base(DeclarativeBase):
    pass

def init_db() -> None:
    Base.metadata.create_all(db)
