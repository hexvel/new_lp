import asyncio

from vkbottle.user import User as VKUser

from models.db_user import User


class UserManager:
    def __init__(
        self,
        controller,
        user: User,
        loop: asyncio.AbstractEventLoop,
        session: VKUser,
    ):
        self.user = user
        self.loop = loop
        self.session = session
        self.controller = controller

        # User models
        self.user_id = None
        self.token = None

    async def initialize(self):
        self.user_id = self.user.user_id
        self.token = self.user.token

    def get_prefix_commands(self):
        return ".д"

    async def start(self):
        self.loop = self.loop.create_task(
            self.session.run_polling(), name=f"user_{self.user_id}"
        )

    async def restart(self):
        self.loop.cancel()
        await self.start()

    async def stop(self):
        self.loop.cancel()
