from os import name
from fastapi import responses
from fastapi import websockets
from fastapi.exceptions import HTTPException
from fastapi.responses import PlainTextResponse
from starlette.responses import HTMLResponse
from exceptions import StoryException
from fastapi import FastAPI
from routers import blog_get, blog_post, user, article, product, file, dependencies
from auth import authentication
from templates import templates
from db import models
from db.database import engine
from fastapi import Request
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
import time
from client import html
from fastapi.websockets import WebSocket

app = FastAPI()
app.include_router(templates.router)
app.include_router(dependencies.router)
app.include_router(authentication.router)
app.include_router(file.router)
app.include_router(user.router)
app.include_router(article.router)
app.include_router(product.router)
app.include_router(blog_get.router)
app.include_router(blog_post.router)


@app.get("/hello")
def index():
    return {"message": "Hello world!"}


@app.exception_handler(StoryException)
def story_exception_handler(request: Request, exc: StoryException):
    return JSONResponse(status_code=418, content={"detail": exc.name})


@app.get("/")
async def get():
    return HTMLResponse(html)


clients = []


@app.websocket("/chat")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    clients.append(websocket)
    while True:
        data = await websocket.receive_text()
        for client in clients:
            await client.send_text(data)


# @app.exception_handler(HTTPException)
# def custom_handler(request: Request, exc: StoryException):
#   return PlainTextResponse(str(exc), status_code=400)

# Creando la DB
models.Base.metadata.create_all(engine)


# los middleware permite darle manejo a las request y responses, tambien,
# agrega funcionalidades estandar a los endpoints de la ruta seleccionada como lo es
# 'duration' que determina el tiempo de respuesta del endpoint al enviar data
# se puede ver en el navegador en la parte de network
@app.middleware("/http")
async def add_middleware(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    duration = time.time() - start_time
    response.headers["duration"] = str(duration)
    return response


origins = ["http://localhost:3000"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Permite que los archivos cargados por endpoint file, se puedan acceder por el navegador con su
# respectivo endpoint y nombre del archivo localhost/files/<nombre del archivo y extension>
app.mount("/files", StaticFiles(directory="files"), name="files")
app.mount("/templates/static", StaticFiles(directory="templates/static"), name="static")
