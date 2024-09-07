from models.user import UserModel
from service.user import UserService


class DB_DATA:
    HOST = "localhost"


class CONTROLLER:
    USERS = {}

    @classmethod
    def set_user(cls, user_id: int, service: UserService):
        cls.USERS[user_id] = service

    @classmethod
    def get_user(cls, user_id: int) -> UserModel:
        return cls.USERS.get(user_id)

    @classmethod
    async def start_user(cls, user_id: int):
        await cls.USERS[user_id].manager.start()

    @classmethod
    async def restart_user(cls, user_id: int):
        await cls.USERS[user_id].manager.restart()

    @classmethod
    async def stop_user(cls, user_id: int):
        await cls.USERS[user_id].manager.stop()
