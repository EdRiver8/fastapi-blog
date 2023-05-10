CONFIGURACION INICIAL
1- Instalar el ambiente virtual(venv): python -m venv /path/to/new/virtual/environment, la ruta es el
lugar y el nombre(ultima parte de la ruta) del proyecto, si ya se esta en la carpeta donde se va a crear
el venv, despues de 'venv' solo se pone el nombre del ambiente virtual (puede ser el nombre del proyecto)
2- Activar el venv en win (ubicado en la carpeta padre del venv): <venv>\Scripts\activate.bat <>primera parte,
es el nombre del ambiente virtual (paso anterior).
3- Instalar fastapi: pip install fastapi
4- Instalar el servidor: pip install uvicorn
5- Ejecutar el servidor: uvicorn (Lugar donde encuentra la instancia de fastapi)main:(nombre de la instancia)app --reload (cambios reiniciar)
6- Documentacion de los endpoints: http://127.0.0.1:8000/docs generada posr swagger o http://127.0.0.1:8000/redoc
