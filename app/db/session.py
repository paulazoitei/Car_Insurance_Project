from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os
import psycopg2
load_dotenv()
engine=create_engine(os.getenv("DATABASE_URL"))
SessionLocal=sessionmaker(autocommit=False,autoflush=False,bind=engine)


def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()