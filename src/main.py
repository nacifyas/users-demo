import uvicorn
from models.user import User
from dal.userdal import UserDAL
from aredis_om import NotFoundError
from fastapi import FastAPI, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_methods=['*'],
    allow_headers=['*']
)


@app.get('/{primary_key}', response_model=User, status_code=status.HTTP_200_OK)
async def get_user_by_id(primary_key: str) -> User:
    """ Given a primary key, will return the correspondig
    user if found.

    Args:
        primary_key (str): User primary key

    Raises:
        HTTPException: 404 error if such user is not found

    Returns:
        User: The corresponding user
    """
    try:
        return await UserDAL().get_user_by_primary_key(primary_key)
    except NotFoundError:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )


@app.get('/', response_model=list[User], status_code=status.HTTP_200_OK)
async def get_all_users(offset: int = 0, limit: int = 50) -> list[User]:
    """ Returns an array of all users, delimited by the offset
    and limit argument

    Args:
        offset (int, optional): Amount of users to skip. Defaults to 0.
        limit (int, optional): Max amount of users to return. Defaults to 50.

    Returns:
        list[User]: list of all the users
    """
    return UserDAL().get_all_users(offset, limit)
    

@app.post('/', response_model=User, status_code=status.HTTP_201_CREATED)
async def create_user(user: User) -> User:
    """ Gets an User object and adds it to the database

    Args:
        user (User): User data, without pk and status fields

    Returns:
        User: The just created user with all its fields
    """
    return await UserDAL().create_user(user)


@app.delete('/{primary_key}', status_code=status.HTTP_202_ACCEPTED)
async def delete_user(primary_key: str) -> int:
    """ Given an user's primary key, it deletes it

    Args:
        primary_key (str): User's primary key

    Returns:
        int: 1 if deletion was performed
             0 otherwise
    """
    return await UserDAL().delete_user(primary_key)


if __name__ == '__main__':
    uvicorn.run("main:app", port=8001, reload=True, host="127.0.0.1")
