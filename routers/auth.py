
from schema.users import User

from fastapi import(
    APIRouter, Body, Form, status, HTTPException
) 


auth = APIRouter()

@auth.post(
    path='/auth/login',
    status_code=status.HTTP_200_OK,
    response_model=User,
    response_model_exclude={'passwd'},
    tags=['Auth']
)
def login(
    email:str = Form(...,min_length=3),
    passwd:str = Form(...,min_length=8)
):
    return {
        'email':email,
        'passwd':passwd
    }

