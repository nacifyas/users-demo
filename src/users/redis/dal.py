from users.models.user import UserRead, UserCreate, UserUpdate
from users.redis.conf import redis_sync_connection as redis
import asyncio

class UserDAL:
    async def get(self, id: str) -> UserRead:
        return await redis.json().get(f"user:{id}")

    async def create(self, user: UserCreate) -> int:
        return await redis.json().set(f"user:{user.id}", user, path=".")

    async def delete(self, id: str) -> int:
        return await redis.json().forget(f"user:{id}")

    async def update(self, user: UserUpdate) -> int:
        coro_arr = []
        if user.username is not None:
            coro_arr.append(
                redis.json().set(f"user:{user.id}", user.username, path=".username")
            )
        if user.age is not None:
            coro_arr.append(
                redis.json().set(f"user:{user.id}", user.age, path=".age")
            )
        if user.password is not None:
            coro_arr.append(
                redis.json().set(f"user:{user.id}", user.password, path=".password")
            )
        return await asyncio.gather(**coro_arr)

    async def get_all(self) -> list[UserRead]:
        return await redis.ft().search(f"*")

    async def get_by_username(self, username: str) -> list[UserRead]:
        return await redis.ft().search(f"{username}")
