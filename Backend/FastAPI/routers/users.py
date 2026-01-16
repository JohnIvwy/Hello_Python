# -------------------------------------------------------------------------------------------------
# Creando un API (CRUD) para usuarios
# -------------------------------------------------------------------------------------------------

from fastapi import APIRouter, HTTPException

# Creación de instancia
router = APIRouter(prefix='/users',
                   tags=['users'],
                   responses={404: {'message':'No encontrado'}})

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
            User(id=3, name='Diana', surname='Vanegas', age=35),
            User(id=4, name='Paula', surname='Useche', age=20),
            ]


# Petición al servidor
@router.get('/')
async def users():
    return users_ls


# Petición al servidor por PATH con el id del usuario (url: /user/1/john...)
@router.get('/{id}')
async def user(id: int):
    return search_user(id)


# Petición al servidor por QUERY (url: /user/?id=1&name=john...)
@router.get('/')
async def user(id: int):
    return search_user(id)


# Función para buscar usuario por id
def search_user(id: int):
    users = list(filter(lambda user: user.id == id, users_ls))
    try:
        return users[0]
    except:
        return {'error':'No se encontró ningún usuario'}


# En conclusión: podemos definir algunos parámetros como:
# Parámetros requeridos: ya sea por path o por query.
# Parámetros con un valor por defecto: definimos su valor con el =
# Parámetros enteramente opcionales: cuando los definimos con | None = None
#   str | None significa que la variable es de tipo str pero también podría ser None, 
#   = None significa que definimos el valor por defecto None, 
#   así que FastAPI sabrá que no es requerido.

@router.get("/items/{item_id}")
async def read_user_item(
    item_id: str, 
    needy: str, 
    skip: int = 0, 
    limit: int | None = None
):
    item = {"item_id": item_id, "needy": needy, "skip": skip, "limit": limit}
    return item


# -------------------------------------------------------------------------------------------------

# Método POST
# Un request body es un dato enviado por el cliente a tu API. 
# Un response body es el dato que tu API envía al cliente.

@router.post('/', response_model=User, status_code=201)
async def user(user: User):
    if type(search_user(user.id)) == User:
        raise HTTPException(status_code=404, detail='El usuario ya existe')
    
    users_ls.append(user)
    return user

# Códigos de estado HTTP: 
# Informational responses (100 – 199)
# Successful responses (200 – 299)
# Redirection messages (300 – 399)
# Client error responses (400 – 499)
# Server error responses (500 – 599)


# -------------------------------------------------------------------------------------------------

# Método PUT (update)

@router.put('/')
async def user(user: User):

    found = False

    for index, saved_user in enumerate(users_ls):
        if saved_user.id == user.id:
            users_ls[index] = user
            found = True

    if not found:
        return {'error': 'No se ha actualizado el usuario'}
    
    return user


# -------------------------------------------------------------------------------------------------

# Método DELETE

@router.delete('/{id}')
async def user(id:int):

    delete = False
    
    for index, saved_user in enumerate(users_ls):
        if saved_user.id == id:
            del users_ls[index]
            delete = True

    if not delete:
        {'error':'No se ha eliminado'}
