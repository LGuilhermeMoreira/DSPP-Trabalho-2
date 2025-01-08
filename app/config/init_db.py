# app/config/init_db.py
from sqlmodel import SQLModel, create_engine
from .config import settings
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

def create_db_and_tables():
    engine = create_engine(settings.DATABASE_URL, echo=True)
    SQLModel.metadata.create_all(engine)
    return engine
