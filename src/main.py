import uvicorn
from dal.userdal import UserDAL
from models.user import User, UserCreate, UserRead
from fastapi import FastAPI, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from bson.errors import InvalidId

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_methods=['*'],
    allow_headers=['*']
)


@app.get('/{primary_key}', response_model=UserRead, status_code=status.HTTP_200_OK)
async def get_user_by_id(primary_key: str) -> UserRead:
    """ This endpoint retrieves the user given its id

    Args:
        primary_key (str): user primary key or id

    Raises:
        HTTPException: With the error 404 if such user
        does not exist
        HTTPException: With the error 406 if the provided
        id is not properfly formated

    Returns:
        User: User with all its fields
    """
    try:
        user = UserDAL().get_user_by_id(primary_key)
        if user is not None:
            return user
        else:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="User not found"
            )
    except InvalidId:
        raise HTTPException(
            status_code=status.HTTP_406_NOT_ACCEPTABLE,
            detail="Not a valid ID"
        )        


@app.get('/', response_model=list[UserRead], status_code=status.HTTP_200_OK)
async def get_all_users(offset: int = 0, limit: int = 50) -> list[UserRead]:
    return UserDAL().get_all_users(offset, limit)


@app.post('/', response_model=UserRead, status_code=status.HTTP_201_CREATED)
async def create_user(user_create: UserCreate) -> UserRead:
    return UserDAL().create_user(user_create)


@app.delete('/{primary_key}', status_code=status.HTTP_202_ACCEPTED)
async def delete_user(primary_key: str) -> int:
    try:
        return UserDAL().delete_user(primary_key)
    except InvalidId:
        raise HTTPException(
            status_code=status.HTTP_406_NOT_ACCEPTABLE,
            detail="Not a valid ID"
        )     

if __name__ == '__main__':
    uvicorn.run("main:app", port=8001, reload=True, host="127.0.0.1")
