from uuid import UUID
from datetime import date
from typing import Optional
from enum import Enum

class Gender(str, Enum):
    MALE = 'Male'
    FEMALE = 'Female'
    OTHER = 'Other'


from pydantic import(
    BaseModel, EmailStr, Field
)

class User(BaseModel):
    user_id: UUID = Field(default=None)
    email: EmailStr = Field(...)
    passwd: str = Field(
        ...,
        min_length=8
    )
    first_name:str = Field(
        ...,
        min_length=2,
        max_length=50
    )
    last_name:str = Field(
        ...,
        min_length=2,
        max_length=50
    )
    birth_date: Optional[date] = Field(
        example=date.today(),
        default=None
    )
    gender: Optional[Gender] = Field(
        default=None,
        example=Gender.MALE
    )