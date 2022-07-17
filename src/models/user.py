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
    """ Recieves a document (mongodb object querried)
    and turns it into a UserRead

    Args:
        document: mongodb querry document

    Returns:
        UserRead: Equivalent UserRead model of the document
    """
    if document is not None:
        return UserRead(**
            {
                "pk": str(document["_id"]),
                "username": document["username"],
                "password": document["password"],
                "status": document["status"]
            }
        )
