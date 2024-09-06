from typing import Any, Coroutine, Union

from pydantic import BaseModel


class UserModel(BaseModel):
    user_id: Union[int, None] = None
    token: Union[str, None] = None

    @property
    async def start_user(self) -> Coroutine[Any, Any, None]: ...
    @property
    async def restart_user(self) -> Coroutine[Any, Any, None]: ...
    @property
    async def stop_user(self) -> Coroutine[Any, Any, None]: ...
