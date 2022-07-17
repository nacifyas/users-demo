from aredis_om import get_redis_connection

STREAM_URL = f"redis://atomflare.af:6388"

redis_stream = get_redis_connection(
    url=STREAM_URL,
    encoding=ENCODING,
    decode_responses=True,
    db=1
)