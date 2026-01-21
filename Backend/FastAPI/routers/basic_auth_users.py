from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel
# OAuth2PasswordBearer se encarga de gestionar la autenticación
# OAuth2PasswordRequestForm para obtener el usuario y contraseña de un formulario
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

router = APIRouter()

# Instancia de nuestro sistema de autenticación OAuth2
oauth2 = OAuth2PasswordBearer(tokenUrl='login')

class User(BaseModel):
    username: str
    full_name: str
    email: str
    disable: bool

class UserDB(User):
    password: str

users_db = {
    'John':{
        'username':'JohnL', 
        'full_name':'John Leon', 
        'email':'leon@dev.com', 
        'disable':False, 
        'password':'1'
    },
    'Antonio':{
        'username':'AntonioL', 
        'full_name':'Antonio Leon', 
        'email':'thony@dev.com', 
        'disable':True, 
        'password':'2'
    }
}
    
# Función para buscar usuario en la base de datos
def search_user_db(username: str):
    if username in users_db:
        return UserDB(**users_db[username])

def search_user(username: str):
    if username in users_db:
        return User(**users_db[username])
    
# Función para validar la autenticación del usuario
async def current_user(token: str = Depends(oauth2)):
    user = search_user(token)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, 
            detail='Credenciales de autenticación inválidas', 
            headers={'WWW-Authenticate': 'Bearer'})
    
    if user.disable:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, 
            detail='Usuario inactivo')
    
    return user
    
@router.post('/login')
# Recibiremos un parámetro de tipo "OAuth2PasswordRequestForm"
async def login(form: OAuth2PasswordRequestForm = Depends()):
    user_db = users_db.get(form.username)
    if not user_db:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, 
            detail='El usuario no es correcto')

    user = search_user_db(form.username)
    if form.password != user.password:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, 
            detail='La contraseña no es correcta')
    
    # Cuando el usuario se autentica exitosamente, el sistema debe devolver un access token y su tipo
    return {'access_token': user.username, 'token_type': 'bearer'}

@router.get('/users/me')
async def me(user: User = Depends(current_user)):
    return user