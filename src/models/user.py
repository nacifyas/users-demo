from aredis_om import HashModel
from config.redis_conf import redis


class User(HashModel):
    username: str
    age: int
    password: str
    status: str = "PROCESSING"

    class Meta:
        database = redis
