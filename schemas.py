from typing import List
from pydantic import BaseModel


# Article inside UserDisplay
class Article(BaseModel):
    title: str
    content: str
    published: bool

    # permite convertira los tipos de datos de la db (models DbUser) a UserDisplay (objects)
    class Config:
        orm_mode = True


# DTO de Ingreso: datos que se reciben del usuario por los endpoints
class UserBase(BaseModel):
    username: str
    email: str
    password: str


# DTO de salida: informacion que se le regresa al usuario
class UserDisplay(BaseModel):
    username: str
    email: str
    items: List[Article] = []

    # permite convertira los tipos de datos de la db (models DbUser) a UserDisplay (objects)
    class Config:
        orm_mode = True


# User inside ArticleDisplay
class User(BaseModel):
    id: int
    username: str

    class Config:
        orm_mode = True


class ArticleBase(BaseModel):
    title: str
    content: str
    published: bool
    creator_id: int


class ArticleDisplay(BaseModel):
    title: str
    content: str
    published: bool
    user: User

    class Config:
        orm_mode = True


class ProductBase(BaseModel):
    title: str
    description: str
    price: float
