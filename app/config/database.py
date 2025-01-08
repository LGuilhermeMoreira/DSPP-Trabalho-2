from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlmodel import SQLModel
from .config import settings
import sys
try:
    engine = create_engine(settings.DATABASE_URL)
except:
    print("banco de dados não conectado")
    sys.exit()

SQLModel.metadata
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)