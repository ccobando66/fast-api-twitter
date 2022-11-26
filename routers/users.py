from cryptography.fernet import Fernet
from typing import List
import uuid


from schema.users import User

from models.users import Users

from config.config import(
    conexion, Session, Base
)

from fastapi import(
    APIRouter, status, Body,
    Path, HTTPException
    
)

users = APIRouter()

key = Fernet.generate_key()
cif = Fernet(key)


Base.metadata.create_all(conexion)
session = Session()


@users.get(
    path='/users',
    status_code=status.HTTP_200_OK,
    tags=['User']
)
def get_all_users():
    all_users = session.query(Users).all()
    session.close
    return all_users


@users.get(
    path='/users/{user_id}',
    status_code=status.HTTP_200_OK,
    tags=['User']
)
def get_user(user_id:str = Path(...,min_length=3)):
    
    userts = session.query(Users).get(user_id)
    session.close()
    if userts is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='user not exists')
    return userts
    
    


@users.post(
    path='/users',
    status_code=status.HTTP_201_CREATED,
    response_model=User,
    response_model_exclude={'passwd'},
    tags=['User']
)
def create_users(user:User = Body(...)):
    
    user.user_id = uuid.uuid4()
    user.passwd = cif.encrypt(user.passwd.encode('utf-8'))
    user_recived = Users(
        id=user.user_id,
        email=user.email,
        passwd=user.passwd,
        first_name=user.first_name,
        last_name=user.last_name
    )
    session.add(user_recived)
    session.commit()
    session.close()
    
    return user



@users.put(
    path='/users/{user_id}',
    status_code=status.HTTP_200_OK,
    tags=['User']
)
def update_user(
    user_id:str = Path(
        ...,
        min_length=3
        ),
    user:User=Body(...)
):
    user_recived = session.query(Users).get(user_id)
    if user_recived is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='user not exists')
    user_recived.first_name = user.first_name
    user_recived.last_name = user.last_name
    session.add(user_recived)
    session.commit()
    session.close()
    return user
    


@users.delete(
    path='/users/{user_id}',
    status_code=status.HTTP_200_OK,
    tags=['User']
)
def delete_user(
    user_id:str = Path(
        ...,
        min_length=3
        )
):
    deleted_user = session.query(Users).get(user_id)
    if deleted_user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='user not exists')
    session.delete(deleted_user)
    session.commit()
    session.close()
    return deleted_user
