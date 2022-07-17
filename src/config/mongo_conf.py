from pymongo import MongoClient

TIMEOUT = 6000
DATABASE = "users_microservice"
COLLECTION = "users"
USERNAME = "root"
SECRET = "secret"
HOST = "atomflare.af"
PORT = 27017

mongoDB_url = f"mongodb://{USERNAME}:{SECRET}@{HOST}:{PORT}/?authMechanism=DEFAULT"

mongo_connection = MongoClient(
    mongoDB_url,
    tz_aware=True
)

db = mongo_connection[DATABASE]
collection = db[COLLECTION]