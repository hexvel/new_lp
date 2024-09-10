from models.user_pydantic import UserModel

TORTOISE_ORM = {
    "connections": {"default": "mysql://**:***@***:3306/***"},
    "apps": {
        "models": {
            "models": ["models.user"],
            "default_connection": "default",
        },
    },
}


class Settings:
    USERS = {}

    @classmethod
    def set_user(cls, user_id: int, service):
        """
        Set user by id.

        Args:
            user_id (int): User id.
            service (Service): User service.
        """
        cls.USERS[user_id] = service

    @classmethod
    def get_user(cls, user_id: int) -> UserModel:
        """
        Get user by id.

        Args:
            user_id (int): User id.

        Returns:
            UserModel: User model or None if user not found.
        """
        return cls.USERS.get(user_id)

    @classmethod
    async def start_user(cls, user_id: int):
        """
        Start user by id.

        Args:
            user_id (int): User id.
        """
        user = cls.get_user(user_id)
        if user:
            await user.manager.start()
        else:
            print("User not found.")

    @classmethod
    async def stop_user(cls, user_id: int):
        """
        Stop user by id.

        Args:
            user_id (int): User id.
        """

        user = cls.get_user(user_id)
        if user:
            await user.manager.stop()
        else:
            print("User not found.")

    @classmethod
    async def restart(cls, user_id: int):
        """
        Restart user by id.

        Args:
            user_id (int): User id.
        """

        await cls.stop_user(user_id)
        await cls.start_user(user_id)
