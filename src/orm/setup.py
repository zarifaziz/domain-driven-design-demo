# src/orm/setup.py
# responsible for setting up the database connection and creating the table

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from .mapper import metadata, start_mappers

DATABASE_URL = "sqlite:///:memory:"
engine = create_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(bind=engine)


def init_db():
    start_mappers()
    metadata.create_all(engine)
