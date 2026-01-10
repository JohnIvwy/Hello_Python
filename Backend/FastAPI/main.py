# Tenemos que importar el framework FastAPI

# FastAPI es una clase de Python que proporciona toda la funcionalidad para la API.
from fastapi import FastAPI

# Creamos una instancia u objeto de FastAPI
app = FastAPI()

# Declaramos Path Operation Function a nuestra API

# la declaramos asíncrona con 'async' para que la función se ejecute en segundo plano
# y que nuestra web funcione aunque todavía no halla recibido la respuesta que solicitó.
# Petición get a nuestro servidor. Entre parentesis colocamos el Path ("endpoint" o "ruta")

# El decorador @app.get("/") le dice a FastAPI que la función justo debajo se encarga de 
# manejar requests que vayan a el path / usando un método u operación get

@app.get('/') 
async def root():
    return '¡Hola FastAPI!'

# Así hemos declarado nuestra Path Operation Function
# path: es /. 
# operation: es get. 
# function: es la función debajo del "decorador" (debajo de @app.get("/")).


@app.get('/url')
async def url():
    return {'url_curso':'https://mouredev.com/python'}

# Iniciamos el servidor escribiendo en la terminal: uvicorn nombre_archivo:nombre_instancia --reload
# reload para que se recargue cada vez que hagamos un cambio en el fichero
# Detener el server: CTRL+C

# -----------------------------------------------------------------------------------------------------

# Postman un cliente para poder ejecutar peticiones a una API, para poder interactuar con Backend (API)

# Peticiones o métodos HTTP a una API:

# GET: leer datos
# POST: crear datos
# PUT: actualizar datos
# DELETE: borrar datos
