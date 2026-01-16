from fastapi import APIRouter

router = APIRouter(prefix='/products', 
                   tags=['products'],
                   responses={404: {'message':'No encontrado'}})

products_ls = ['Pdt 1','Pdt 2','Pdt 3']

@router.get('/')
async def products():
    return products_ls

@router.get('/{id}')
async def products(id: int):
    return products_ls[id]


