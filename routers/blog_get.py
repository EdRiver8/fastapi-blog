from typing import Optional
from fastapi import APIRouter, Response, status
from enum import Enum

router = APIRouter(prefix="/blog", tags=["blog"])


#     """Get all, debe ir primero que la otra ruta con la que comparte el mismo nombre /blog{id},
#     porque el orden importa en los endpoints que se definan
#     """
# @app.get("/blog/all")
# def get_all_blogs():
#     return {"message": "All blogs"}


# tags permite agrupar los endpoints por categorias y mejorar la documentacion
# Summary y Description mejora la documentacion de la api
@router.get(
    "/all",
    summary="Retrieve all blog",
    description="This api call simulates fetching all blogs",
    response_description="The list of avalible blogs",
)
def get_all_blogs(page=1, page_size: Optional[int] = None):
    """Usando Query params y valores por defecto"""
    return {"message": f"All {page_size} blogs on page {page}"}


@router.get("/{id}/comments/{comment_id}", tags=["comment"])
def get_comment(
    id: int, comment_id: int, valid: bool = True, username: Optional[str] = None
):
    """
    Simulates retrieving a comment of a blog

    - **id** mandatory path param
    - **comment_id** mandatory path param
    - **valid** Optional query param
    - **username** Optional query param
    """
    return {
        "message": f"blog_id {id}, comment_id {comment_id}, valid {valid}, username {username}"
    }


class BlogType(str, Enum):
    # Hereda de Enum
    short = "short"
    story = "story"
    howto = "howto"


@router.get("/type/{type}")
def get_blog_type(type: BlogType):
    # type valor predefinido que viene de la clase Enum por BlogType
    return {"message": f"Blog type {type}"}


# @router.get("/blog/{id}", status_code=404)
@router.get("/{id}", status_code=status.HTTP_200_OK)
def get_blog(id: int, response: Response):
    """Usando Path Param variables"""
    if id > 5:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"error": f"Blog {id} not found"}
    else:
        response.status_code = status.HTTP_200_OK
        return {"message": f"Blog with id {id}"}
