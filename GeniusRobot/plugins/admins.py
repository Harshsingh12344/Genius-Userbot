import time

from pyrogram import filters, Client
from pyrogram.errors import UserAdminInvalid
from pyrogram.types import Message, ChatPermissions

from GeniusRobot.config import *
from GeniusRobot.plugins.help import *
from GeniusRobot.modules.helpers.filters import *
from GeniusRobot.modules.helpers.program import GetUserMentionable
from GeniusRobot.modules.helpers.admins import CheckAdmin, CheckReplyAdmin, RestrictFailed




@Client.on_message(command("kick") & genius_filters)
async def kick_user(bot: Client, message: Message):
    if await CheckReplyAdmin(message) and await CheckAdmin(message):
        try:
            mention = GetUserMentionable(message.reply_to_message.from_user)

            await bot.kick_chat_member(
                chat_id=message.chat.id,
                user_id=message.reply_to_message.from_user.id,
            )

            await message.edit(f"Goodbye, {mention}.")
        except UserAdminInvalid:
            await RestrictFailed(message)


add_command_help(
    "ban",
    [
        [".ban", "Bans user for specified hours or indefinitely."],
        [".unban", "Unbans the user."],
        [".mute", "Bans user for specified hours or indefinitely."],
        [".unmute", "Unmutes the user."],
        [".kick", "Kicks the user out of the group."],
    ],
)
