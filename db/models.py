from sqlalchemy import Column, Integer, String
from db.database import Base

# Estos son los datos que se envian a la DB


class DbUser(Base):
    __tablename__ = "users"  # nombre de la tabla en la db
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(255))
    email = Column(String, unique=True)
    password = Column(String)
