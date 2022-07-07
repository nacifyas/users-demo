import uvicorn
from fastapi import FastAPI

app = FastAPI()

@app.get('/')
async def get_users():
    pass

@app.get('/{user_id}')
async def get_users(user_id):
    pass

@app.post('/')
async def create_user(user):
    pass

@app.put('/')
async def update_user(user):
    pass

@app.delete('/{user_id}')
async def delete_user(user):
    pass

if __name__ == '__main__':
    uvicorn.run("main:app", port=8001, reload=True, host="127.0.0.1")