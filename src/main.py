import asyncio
import uvicorn
from models.user import User
from fastapi import FastAPI, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from aredis_om import NotFoundError, Migrator


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_methods=['*'],
    allow_headers=['*']
)


@app.get('/{primary_key}', response_model=User, status_code=status.HTTP_200_OK)
async def get_user_by_id(primary_key: str) -> User:
    try:
        return await User.get(primary_key)
    except NotFoundError:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )


@app.get('/', response_model=list[User], status_code=status.HTTP_200_OK)
async def get_all_users(offset: int = 0, limit: int = 50) -> list[User]:
    corr_arr = [get_user_by_id(pk) async for pk in await User.all_pks()]
    user_arr = await asyncio.gather(*corr_arr)
    return user_arr[offset:limit]
    

@app.post('/', response_model=User, status_code=status.HTTP_201_CREATED)
async def create_user(user: User) -> User:
    return await user.save()


@app.put('/', response_model=User, status_code=status.HTTP_202_ACCEPTED)
async def update_user(user: User) -> User:
    return await user.save()


@app.delete('/{primary_key}', status_code=status.HTTP_202_ACCEPTED)
async def delete_user(primary_key: str) -> int:
    return await User.delete(primary_key)

if __name__ == '__main__':
    uvicorn.run("main:app", port=8001, reload=True, host="127.0.0.1")
