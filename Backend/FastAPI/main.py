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
