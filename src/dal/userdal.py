from models.user import User, UserCreate, UserRead, normalize
from config.mongo_conf import collection
from bson import ObjectId


class UserDAL():
    """ This class offer abstraction to interact with
    the mongoDB database more easily.

    This interface is CRUD centric, meaning that it only performs
    the operation suggested by each method name, with no side effects
    """
    def get_user_by_id(self, primary_key: str) -> UserRead:
        """ Given a user primary key, it retrieves the user

        Args:
            primary_key (str)

        Returns:
            UserRead
        """
        document = collection.find_one({"_id": ObjectId(primary_key)})
        user = normalize(document)
        return user


    def get_all_users(self, offset: int = 0, limit: int = 50) -> list[UserRead]:
        """ Retrieves all the users in the database

        Args:
            offset (int, optional): Number of users to skip. Defaults to 0.
            limit (int, optional): Maximum number of users to return. Defaults to 50.

        Returns:
            list[UserRead]: List of all the users according to the offset and limit
        """
        docs_arr = collection.find(skip=offset, limit=limit)
        user_arr = [normalize(user_doc) for user_doc in docs_arr]
        return user_arr


    def create_user(self, user_create: UserCreate) -> UserRead:
        """ Adds a new user to the database, if validation succeed

        Args:
            user_create (UserCreate): User data according to the
            UserCreate model

        Returns:
            UserRead: The created user with all its fields
        """
        user_data = User(**user_create.dict())
        user_id = collection.insert_one(user_data.dict()).inserted_id
        user = self.get_user_by_id(user_id)
        return user


    def delete_user(self, primary_key: str) -> int:
        """ Proceeds with the deletion of the user given its primary_key

        Args:
            primary_key (str): User's primary key

        Returns:
            int: Number of entries deleted
        """
        return collection.delete_one({"_id": ObjectId(primary_key)}).deleted_count
