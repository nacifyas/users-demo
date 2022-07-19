from models.user import User
import asyncio


class UserDAL():
    """ This class abstracts from the endpoints section all
    the database access and operation in order to keep the
    endpoints section more clean.
    The following methods are Data Access Layer centric with
    no side effects, meaning that they perform exactly the
    transaction suggested by the method name and the docstring,
    thus they are very specialized in their task with no side
    effects
    """

    
    async def get_all_users(self, offset: int = 0, limit: int = 50) -> list[User]:
        """ Returns an array of all users, delimited by the offset
        and limit argument

        Args:
            offset (int, optional): Amount of users to skip. Defaults to 0.
            limit (int, optional): Max amount of users to return. Defaults to 50.

        Returns:
            list[User]: list of all the users
        """
        corr_arr = [self.get_user_by_primary_key(pk) async for pk in await User.all_pks()]
        user_arr = await asyncio.gather(*corr_arr)
        return user_arr[offset:limit]


    async def get_user_by_primary_key(self, primary_key: str) -> User:
        """ Given a primary key, will return the correspondig
        user if found.

        Args:
            primary_key (str): User primary key

        Returns:
            User: The corresponding user
        """
        return await User.get(primary_key)

    
    async def create_user(user: User) -> User:
        """ Gets an User object and adds it to the database

        Args:
            user (User): User data, without pk and status fields

        Returns:
            User: The just created user with all its fields
        """
        return await user.save()


    async def delete_user(primary_key: str) -> int:
        """ Given an user's primary key, it deletes it

        Args:
            primary_key (str): User's primary key

        Returns:
            int: 1 if deletion was performed
                 0 otherwise
        """
        return await User.delete(primary_key)
