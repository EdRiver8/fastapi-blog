from typing import Dict, List, Optional
from fastapi import APIRouter, Body, Query, Path
from pydantic import BaseModel

router = APIRouter(prefix="/blog", tags=["blog"])


class Image(BaseModel):
    url: str | None = None
    alias: str | None = ("xyz",)


class BlogModel(BaseModel):
    title: str
    content: str
    nb_comments: int
    published: Optional[bool]
    tags: List[str] = []  # temas de interes
    metadata: Dict[str, str] = {"key": "value"}
    image: Optional[Image] | None = None


@router.post("/new/{id}")
def create_blog(blog: BlogModel, id: int, version: int = 1):
    return {"id": id, "data": blog, "version": version}


@router.post("/new/{id}/comment/{comment_id}")
def create_comments(
    blog: BlogModel,
    id: int,
    comment_title: int = Query(
        None,
        title="Title of the comment",
        description="Decription of the comment_title",
        alias="commentTitle",  # como se va a ver en el nombre del endpoint en la url
        deprecated=True,  # alerta por si algun atributo esta obsoleto
    ),
    # content: str = Body("Hi from body"),
    content: str = Body(..., min_length=10, max_length=15, regex="^[a-z\s]*$"),
    # v: Optional[List[str]] = Query(None),
    v: Optional[List[str]] = Query(["1.0", "1.1", "1.2", "1.3"]),
    comment_id: int = Path(gt=5, le=10),
):
    return {
        "blog": blog,
        "id": id,
        "comment_title": comment_title,
        "content": content,
        "version": v,
        "comment_id": comment_id,
    }


# Ejemplo de dependencia
def requiered_funcionality():
    return {"message": "Learning FastAPI is important"}
