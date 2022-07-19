import pytest
from config.redis_conf import redis, redis_stream


@pytest.mark.asyncio
async def test_db():
    """ Tests if the database
    connection is functioning
    """
    assert await redis.ping() == True


@pytest.mark.asyncio
async def test_stream():
    """ Tests if the streams
    connection for pub-sub for
    events sourcing is functioning
    """
    assert await redis_stream.ping() == True
