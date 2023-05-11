CONFIGURACION INICIAL
1- Instalar el ambiente virtual(venv): python -m venv /path/to/new/virtual/environment, la ruta es el
lugar y el nombre(ultima parte de la ruta) del proyecto, si ya se esta en la carpeta donde se va a crear
el venv, despues de 'venv' solo se pone el nombre del ambiente virtual (puede ser el nombre del proyecto)
2- Activar el venv en win, usar terminal cmd (ubicado en la carpeta padre del venv): <venv>\Scripts\activate.bat <>primera parte,
es el nombre del ambiente virtual (paso anterior).
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
