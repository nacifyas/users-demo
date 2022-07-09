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


@app.get('/{pk}')
def get_by_id(pk):
    return User.get(pk)


@app.get('/')
async def get_all():
    return [get_by_id(pk) for pk in User.all_pks()]


@app.post('/')
async def create(user: User):
    return user.save()


@app.put('/')
async def update_user(user: User):
    return user.save()


@app.delete('/{pk}')
async def delete_user(pk: str):
    return User.delete(pk)


if __name__ == '__main__':
    uvicorn.run("main:app", port=8001, reload=True, host="127.0.0.1")