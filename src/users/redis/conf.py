# import redis.asyncio as redis_async
import asyncio
import redis

REDIS_HOST = "atomflare.af"
REDIS_PORT = "6388"
ENCODING = "utf-8"

# SYNC
redis_sync_connection = redis.StrictRedis(
    REDIS_HOST,
    REDIS_PORT,
    charset=ENCODING,
    decode_responses=True
)

# # ASYNC
# async def connect():
#     return await redis_async.from_url(
#     f"redis://{REDIS_HOST}:{REDIS_PORT}",
#     encoding=ENCODING,
#     decode_responses=True
#     )

# redis_async_connection = asyncio.run(connect())