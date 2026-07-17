from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DB_URL = "mysql+pymysql://Ntdung:123456@localhost:3306/students_management_system"

engine = create_engine(DB_URL)

Base = declarative_base()

SessionLocal = sessionmaker(autoflush= False, autocommit= False, bind= engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()