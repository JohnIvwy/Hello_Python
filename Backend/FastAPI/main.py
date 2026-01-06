# Tenemos que importar el framework FastAPI

from fastapi import FastAPI

# Creamos una instancia de FastAPI
app = FastAPI()

# Declaramos una función a nuestra API
# la declaramos asíncrona con 'async' para que la función se ejecute en segundo plano
# que la app funcione aunque el servidor no me halla respondido una llamada a una función.

@app.get('/') # Petición get a nuestro servidor
async def root():
    return '¡Hola FastAPI!'


@app.get('/url')
async def url():
    return {'url_curso':'https://mouredev.com/python'}

# Iniciamos el servidor escribiendo en la terminal: uvicorn nombre_archivo:nombre_instancia --reload
# reload para que se recargue cada vez que hagamos un cambio en el fichero
# Detener el server: CTRL+C

# -----------------------------------------------------------------------------------------------------

# Postman un cliente para poder ejecutar peticiones a una API, para poder interactuar con Backend (API)

# Peticiones HTTP a una API:

# GET: leer datos
# POST: crear datos
# PUT: actualizar datos
# DELETE: borrar datos
