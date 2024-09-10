import asyncio

from loguru import logger
from vkbottle.api import API
from vkbottle.user import User as Session
from vkbottle.user import UserLabeler

from actions.user import user_labelers
from manager.user import UserManager
from models.user_pydantic import User


class UserService:
    def __init__(self, user: User) -> None:
        self.user = user
        self.user_id = user.id
        self.loop = asyncio.get_event_loop()

        self.session = None
        self.manager = None

    async def initialize(self):
        logger.debug("Initializing API for user service for user {}", self.user_id)

        api = API(self.user.token)

        user_labeler = UserLabeler()
        for labeler in user_labelers:
            user_labeler.load(labeler)

        self.session = Session(api=api, labeler=user_labeler)
        setattr(self.session.api, "data", self)

        logger.debug("Initializing Managers for user service for user {}", self.user_id)

        self.manager = UserManager(self.user, self.loop, self.session)

        await asyncio.gather(*[manager.initialize() for manager in [self.manager]])

        logger.success("User successfully initialized")
