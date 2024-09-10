from pydantic import BaseModel

from manager.user import UserManager


class UserModel(BaseModel):
    manager: UserManager
