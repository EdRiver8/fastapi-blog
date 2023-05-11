from pydantic import BaseModel


# Estos son los datos que se reciben del usuario por los endpoints
class UserBase(BaseModel):
    username: str
    email: str
    password: str


# DTO con la informacion que se le regresa al usuario
class UserDisplay(BaseModel):
    username: str
    email: str

    # permite convertira los tipos de datos de la db (models DbUser) a UserDisplay
    class Config:
        orm_mode = True
