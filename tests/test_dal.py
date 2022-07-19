import pytest
from models.user import User
from dal.userdal import UserDAL


@pytest.mark.asyncio
async def test_create_valid_user():
    user_data: User = User(
        **{
            "username":"test_user",
            "age":0,
            "password": "test_secret"
        }
    )
    new_user = await UserDAL().create_user(user_data)
    assert new_user is not None


@pytest.mark.asyncio
async def test_create_get_user():
    user_data: User = User(
        **{
            "username":"test_user",
            "age":0,
            "password": "test_secret"
        }
    )
    new_user = await user_data.save()
    dal_querried_user = await UserDAL().get_user_by_primary_key(new_user.pk)
    assert dal_querried_user is not None
