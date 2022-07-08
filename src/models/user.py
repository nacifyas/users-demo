from redis_conf import redis
from redis_om import HashModel
# from typing import Optional
# from fastapi import Query

class User(HashModel):
    username: str
    age: int
    password: str

    class Meta:
        database = redis

# class UserBase(HashModel):
#     id: str
#     username: Optional[str] = Query(..., min_length=3, max_length=25)
#     age: Optional[int]  = Query(..., ge=0, le=150)


# class UserRead(UserBase):
#     pass
  

# class UserCreate(UserBase):
#     password: Optional[str] = Query(..., min_length=3, max_length=25)

#     class Meta:
#         database = redis


# class UserUpdate(HashModel):
#     id : str
#     username: Optional[str] = Query(None, min_length=3, max_length=25)
#     age: Optional[int]  = Query(None, ge=0, le=150)
#     password: Optional[str] = Query(None, min_length=3, max_length=25)