from redis_conf import redis
from redis_om import HashModel

class User(HashModel):
    username: str
    age: int
    password: str

    class Meta:
        database = redis
