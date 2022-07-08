import uvicorn
from fastapi import FastAPI
from models.user import User
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_methods=['*'],
    allow_headers=['*']
)

@app.get('/')
async def get_all():
    return await User.all_pks()


@app.post('/')
async def create(user: User):
    return await user.save()

# @app.get('/')
# async def get_users():
#     return await UserDAL().get_all()

# @app.get('/{user_id}')
# async def get_users(user_id):
#     return await UserDAL().get(user_id)

# @app.get('/username/{username}')
# async def get_users(username):
#     return await UserDAL().get_by_username(username)

# @app.post('/')
# async def create_user(user):
#     return await UserDAL().create(user)

# @app.put('/')
# async def update_user(user):
#     return await UserDAL().update(user)

# @app.delete('/{user_id}')
# async def delete_user(user_id):
#     return await UserDAL().delete(user_id)

if __name__ == '__main__':
    uvicorn.run("main:app", port=8001, reload=True, host="127.0.0.1")