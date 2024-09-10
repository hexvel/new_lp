from fastapi import FastAPI
from loguru import logger
from services.user import UserService
from tortoise import Tortoise

from core.config import TORTOISE_ORM, Settings
from models.user_pydantic import User

logger.disable("vkbottle")


async def lifespan(app: FastAPI):
    await Tortoise.init(TORTOISE_ORM)
    await Tortoise.generate_schemas()

    users = await User.all()

    for user in users:
        service = UserService(user)
        await service.initialize()

        Settings.set_user(user.id, service)
        logger.warning(f"User {user.id} loaded")
        await Settings.start_user(user.id)
        logger.success(f"User {user.id} started")

    yield
    await Tortoise.close_connections()
    logger.error("FastAPI shutting down...")


app = FastAPI(lifespan=lifespan)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000, log_level="warning")
