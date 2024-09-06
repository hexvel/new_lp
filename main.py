from fastapi import FastAPI
from loguru import logger
from tortoise import Tortoise

from core.config import CONTROLLER, DB_DATA
from models.db_user import User
from service.user import UserService

logger.disable("vkbottle")


async def lifespan(app: FastAPI):
    await Tortoise.init(
        db_url=f"mysql://{DB_DATA.USER}:{DB_DATA.PASSWORD}@{DB_DATA.HOST}/{DB_DATA.NAME}",
        modules={"models": ["models.db_user"]},
    )
    await Tortoise.generate_schemas()

    users = await User.all()
    for user in users:
        service = UserService(user=user, controller=CONTROLLER)

        await service.initialize()
        service.controller.set_user(user.user_id, service)
        await service.controller.start_user(user.user_id)

    logger.success("Database connection successful")

    yield
    await Tortoise.close_connections()


app = FastAPI(lifespan=lifespan)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000, log_level="warning")
