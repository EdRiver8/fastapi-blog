CONFIGURACION INICIAL
Obs: pip install -r requirements.txt instala todo lo necesario
1- Instalar el ambiente virtual(venv): python -m venv /path/to/new/virtual/environment, la ruta es el
lugar y el nombre(ultima parte de la ruta) del proyecto, si ya se esta en la carpeta donde se va a crear
el venv, despues de 'venv' solo se pone el nombre del ambiente virtual (puede ser el nombre del proyecto)
2- Activar el venv en win, usar terminal cmd (ubicado en la carpeta padre del venv): <venv>\Scripts\activate.bat
<>primera parte, es el nombre del ambiente virtual (paso anterior). Para desactivar en cmd 'deactivate'
3- Instalar fastapi: pip install fastapi
4- Instalar el servidor: pip install uvicorn
5- Ejecutar el servidor: uvicorn (Lugar donde encuentra la instancia de fastapi)main:(nombre de la instancia)app --reload (cambios reiniciar)
6- Documentacion de los endpoints: http://127.0.0.1:8000/docs generada posr swagger o http://127.0.0.1:8000/redoc
7- El modulo 'routers' contiene todo los enpoints de la api, estos son importados en
el main
8- El request en los endpoint, hace la conversion automatica a JSON y al contrario; este
request es implicito cuando en los atributos del endpoint se pasa una clase
9- FastAPI con el uso de BaseModel de Pydantic, ya hace valiadicion de tipos de datos
10- Path param y Query, se diferencian porque los Path param son normalment atributos
de las clases, mientras que los query pueden ser alguna data especifica que no
necesariamente este en una clase y se muestran en el path del endpoint (url)
11- el uso de 'Query' en los endpoints sirve para manejar la metadata y como se presenta
en los endpoints como opcional, se vuelve un default value, y es el unico que permite
n valores opcionales o por defecto
12- el uso de 'Body' es poner un paramentro por defecto en el endpoint; el uso de
'...', es para hacer requerido, no opcional
13- creacion del archivo 'requirements.txt' el cual se puede ejecutar para instalar todo
lo necesario para correr el proyecto: pip install -r requirements.txt
14- Usando sqlalchemy para crear las tablas de la db, uso de una plantilla para ello
(boilerplate) con las importaciones necesarias y codigo inicial
15- Cadena de conexion a la db de SQlite:
{
"previewLimit": 50,
"driver": "SQLite",
"database": "${workspaceFolder:fastapi-blog}/fastapi-blog.db",
"name": "fastapi-blog"
}
16- passlib y bcrypt, librerias para hashear el password
17- Schemas son las clases u objetos (se relaciona con Entity); mientras que los
models, son tablas de la db (se relaciona con repository o dao, solo que el crud esta en db... ejm db_user, usando
Session de SQLAlchemy.orm); ...Base, hace referencia al DTO de entrada (lo que se espera del usuario)
y Dislplay al DTO de salida (lo que se le va a enviar al usuario)
18- Instalar python-multipart para el uso de forms
19- python-jose permite genera los jwt tokens para la autenticacion con Oauth2
20- despliegue en Deta (free), lo que necesita como minimo es un main.py y requirements.txt (Lista
de librerias que se necesitan); antes de logearse se detiene el servidor y se sale del venv, se instala deta en la
maquina con shell para su ejecucion usando: iwr https://get.deta.dev/cli.ps1 -useb | iex (comando despues de instalar
para ayuda: deta --help) luego, se inicia el venv de nuevo, luego comando: deta login(logearse en deta.sh) y
despues: deta new --python first_micro (en el root del proyecto), leer la documentacion para ver los comandos
necesarios (https://docs.deta.sh/docs/home/)
21- instalar httpx, requests y pytest para las pruebas unitarias, para correr los test en cli = pytest
22- websockets permite la conexion y por ello la comunicacion abierta para enviar y recibir msj
