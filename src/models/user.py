from pydantic import BaseModel


class UserCreate(BaseModel):
    username: str
    password: str

    class Config:
        orm_mode = True


class User(UserCreate):
    status: str = "PROCESSING"


class UserRead(User):
    pk: str


def normalize(document) -> UserRead:
    if document is not None:
        return UserRead(**
            {
                "pk": str(document["_id"]),
                "username": document["username"],
                "password": document["password"],
                "status": document["status"]
            }
        )
