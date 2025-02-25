import os
import asyncio
from pyrogram import Client, filters
from pyrogram.types import Message
from GeniusRobot.modules.clientbot.clientbot import client
from GeniusRobot.modules.helpers.command import commandpro
from GeniusRobot.modules.helpers.decorators import sudo_users_only, errors
from GeniusRobot.plugins.help import *


@Client.on_message(commandpro(["x", "op"]) & filters.private & ~filters.edited)
@sudo_users_only
async def downloader(_, message: Message):
    targetcontent = message.reply_to_message
    downloadtargetcontent = await client.download_media(targetcontent)
    send = await client.send_document("me", downloadtargetcontent)
    os.remove(downloadtargetcontent)




add_command_help(
    "save",
    [
        ["op", "Save Any Self Destruct Photo Or Video To Your Saved Message`."],
    ],
)