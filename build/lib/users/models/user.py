from fastapi import Query
from pydantic import BaseModel
from typing import Optional


class UserBase(BaseModel):
    username: Optional[str] = Query(..., min_length=3, max_length=25)
    age: Optional[int]  = Query(..., ge=0, le=150)


class UserRead(UserBase):
    id: str

    class Config:
        orm_mode = True


class UserCreate(UserBase):
    password : Optional[str] = Query(..., min_length=3, max_length=25)


class UserUpdate(BaseModel):
    id : str
    username: Optional[str] = Query(None, min_length=3, max_length=25)
    age: Optional[int]  = Query(None, ge=0, le=150)
    password : Optional[str] = Query(None, min_length=3, max_length=25)