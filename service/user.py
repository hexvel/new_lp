import asyncio

from loguru import logger
from vkbottle.api import API
from vkbottle.user import User as VKUser
from vkbottle.user import UserLabeler

from actions.user import user_labelers
from manager.user import UserManager
from models.db_user import User


class UserService:
    def __init__(self, user: User, controller):
        self.user = user
        self.controller = controller
        self.loop = asyncio.get_event_loop()

        self.session = None
        self.manager = None

    async def initialize(self):
        logger.debug("Initializing API for user service for user {}", self.user.user_id)

        api = API(self.user.token)

        user_labeler = UserLabeler()
        for labeler in user_labelers:
            user_labeler.load(labeler)

        self.session = VKUser(api=api, labeler=user_labeler)
        setattr(self.session.api, "data", self)

        logger.debug(
            "Initializing Managers for user service for user {}", self.user.user_id
        )

        self.manager = UserManager(self.controller, self.user, self.loop, self.session)

        await asyncio.gather(*[manager.initialize() for manager in [self.manager]])

        logger.success("User successfully initialized")
