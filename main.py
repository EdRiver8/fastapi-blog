from typing import Optional
from fastapi import FastAPI, status
from enum import Enum

app = FastAPI()


@app.get("/hello")
def index():
    # return "Hello World!"
    return {"message": "Hello World!"}


# @app.get("/blog/all")
# def get_all_blogs():
#     """Get all, debe ir primero que la otra ruta con la que comparte el mismo nombre /blog{id},
#     porque el orden importa en los endpoints que se definan
#     """
#     return {"message": "All blogs"}


@app.get("/blog/all")
def get_all_blogs(page=1, page_size: Optional[int] = None):
    """Usando Query params y valores por defecto"""
    return {"message": f"All {page_size} blogs on page {page}"}


@app.get("/blog/{id}/comments/{comment_id}")
def get_comment(
    id: int, comment_id: int, valid: bool = True, username: Optional[str] = None
):
    return {
        "message": f"blog_id {id}, comment_id {comment_id}, valid {valid}, username {username}"
    }


class BlogType(str, Enum):
    # Hereda de Enum
    short = "short"
    story = "story"
    howto = "howto"


@app.get("/blog/type/{type}")
def get_blog_type(type: BlogType):
    # type valor predefinido que viene de la clase Enum por BlogType
    return {"message": f"Blog type {type}"}


# @app.get("/blog/{id}", status_code=404)
@app.get("/blog/{id}", status_code=status.HTTP_404_NOT_FOUND)
def get_blog(id: int):
    """Usando Path Param variables"""
    if id > 5:
        return {"error": f"Blog {id} not found"}
    else:
        return {"message": f"Blog with id {id}"}
