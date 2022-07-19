import requests
from fastapi import status

ROOT = "http://127.0.0.1:8001/"

def test_get_all_users():
    """Tests the endpoint
    http://127.0.0.1:8001/
    which return a list of users
    """
    r = requests.get(ROOT)
    assert r.status_code == status.HTTP_200_OK


def test_get_non_existing_user():
    """Tests the endpoint
    http://127.0.0.1:8001/[non_existing_id]
    which raises a http 404 error
    """
    no_user_id = "no_such_user_ id"
    r = requests.get(f"{ROOT}/no_user_id")
    assert r.status_code == status.HTTP_404_NOT_FOUND