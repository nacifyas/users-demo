import asyncio
from users.redis.conf import redis_async_connection as redis_async
from users.redis.conf import redis_connection as redis
from users.models.user import UserRead, UserCreate, UserUpdate

class UserDAL:
    async def get(self, id: str) -> UserRead:
        await redis.json().get(f"user:{id}")

    async def get_by_username(self, username: str) -> list[UserRead]:
        return await redis.ft().search(username)

    async def get_all(self) -> list[UserRead]:
        print("YEP")

    async def create(self, user: UserCreate) -> int:
        await redis.json().set()

    async def delete(self, id: str) -> int:
        await redis.json().delete(f"user:{id}")

    async def update(self, user: UserUpdate) -> int:
        pass

print(redis.ping())
print(asyncio.run(UserDAL().get("abc")))