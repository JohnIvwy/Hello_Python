# -------------------------------------------------------------------------------------------------
# Creando un API (CRUD) para usuarios
# -------------------------------------------------------------------------------------------------

from fastapi import FastAPI

# Creación de instancia
app = FastAPI()

# -------------------------------------------------------------------------------------------------

# Importaremos de pydantic BaseModel para declarar una Entidad (usuarios)
# BaseModel nos obliga a especificar el tipo de dato y especificar los parámetros que enviamos

from pydantic import BaseModel

# Entidad user
class User(BaseModel):
    name: str
    surname: str
    age: int

# Esta lista simula usuarios de nuestra base de datos
users_ls = [User(name='John', surname='Leon', age=22),
            User(name='Thony', surname='Wolf', age=24),
            User(name='Diana', surname='Vanegas', age=35),]

# Petición al servidor
@app.get('/users')
async def users():
    return users_ls
