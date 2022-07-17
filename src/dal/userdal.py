from models.user import User, UserCreate, UserRead, normalize
from config.mongo_conf import collection
from bson import ObjectId


class UserDAL():
    def get_user_by_id(self, primary_key: str) -> UserRead:
        document = collection.find_one({"_id": ObjectId(primary_key)})
        user = normalize(document)
        return user


    def get_all_users(self, offset: int = 0, limit: int = 50) -> list[UserRead]:
        docs_arr = collection.find(skip=offset, limit=limit)
        user_arr = [normalize(user_doc) for user_doc in docs_arr]
        return user_arr


    def create_user(self, user_create: UserCreate) -> UserRead:
        user_data = User(**user_create.dict())
        user_id = collection.insert_one(user_data.dict()).inserted_id
        user = self.get_user_by_id(user_id)
        return user


    def delete_user(self, primary_key: str) -> int:
        return collection.delete_one({"_id": ObjectId(primary_key)}).deleted_count
