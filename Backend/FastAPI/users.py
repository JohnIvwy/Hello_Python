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
    id: int
    name: str
    surname: str
    age: int

# Esta lista simula usuarios de nuestra base de datos
users_ls = [User(id=1, name='John', surname='Leon', age=22),
            User(id=2, name='Thony', surname='Wolf', age=24),
            User(id=3, name='Diana', surname='Vanegas', age=35),]

# Petición al servidor
@app.get('/users')
async def users():
    return users_ls

# Petición al servidor por PATH con el id del usuario (url: /user/1/john...)
@app.get('/users/{id}')
async def user(id: int):
    return search_user(id)


# Petición al servidor por QUERY (url: /user/?id=1&name=john...)
@app.get('/users/')
async def user(id: int):
    return search_user(id)

# Función para buscar usuario por id
def search_user(id: int):
    users = list(filter(lambda user: user.id == id, users_ls))
    try:
        return users[0]
    except:
        return {'error':'No se encontró ningún usuario'}
