from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "sqlite:///./fastapi-blog.db"  # nombre de la db al final

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()  # variable para crear los models


def get_db():
    db = SessionLocal()
    # intenta proeever la db y al final cierra la conexion
    try:
        yield db
    finally:
        db.close()
