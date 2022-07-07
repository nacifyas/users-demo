import redis.asyncio as redis
import asyncio

REDIS_HOST = "atomflare.af"
REDIS_PORT = "6380"
ENCODING = "utf-8"

# SYNC
redis_connection = redis.StrictRedis(
    REDIS_HOST,
    REDIS_PORT,
    charset=ENCODING,
    decode_responses=True
)

# ASYNC
async def connect():
    return await redis.from_url(
    f"redis://{REDIS_HOST}:{REDIS_PORT}",
    encode=ENCODING,
    decode_responses=True
    )

redis_async_connection = asyncio.run(connect())