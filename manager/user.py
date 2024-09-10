import asyncio

from vkbottle.user import User as Session

from models.user import User


class UserManager:
    def __init__(
        self,
        user: User,
        loop: asyncio.AbstractEventLoop,
        session: Session,
    ) -> None:
        self.user = user
        self.loop = loop
        self.session = session

        # User models
        self.user_id = None
        self.token = None
        self.balance = None
        self.username = None
        self.balance = None
        self.prefix = None
        self.script_prefix = None
        self.admin_prefix = None
        self.clan_tag = None
        self.solved_captchas = None

    async def initialize(self):
        self.user_id = self.user.id
        self.token = self.user.token
        self.balance = self.user.balance
        self.username = self.user.username
        self.prefix = self.user.prefix
        self.script_prefix = self.user.script_prefix
        self.admin_prefix = self.user.admin_prefix
        self.clan_tag = self.user.clan_tag
        self.solved_captchas = self.user.solved_captchas

    async def start(self):
        self.loop = self.loop.create_task(
            self.session.run_polling(), name=f"user_{self.user_id}"
        )

    async def stop(self):
        self.loop.cancel()

    async def restart(self):
        await self.stop()
        await self.start()
