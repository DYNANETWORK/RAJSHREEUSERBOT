import asyncio
from datetime import datetime

from .. import ALIVE_NAME
from ..cmdhelp import CmdHelp
from ..utils import admin_cmd, edit_or_reply, sudo_cmd

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "REBEL User"
REBELOP = borg.uid
REBEL_IMG = "https://telegra.ph/file/5016820bbfdd82f7ef567.jpg"

# PIC ADDED BY MAFIA OWNER

@bot.on(admin_cmd(pattern="ping$", outgoing=True))
@bot.on(sudo_cmd(pattern="ping$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    start = datetime.now()
    event = await edit_or_reply(event, "__**(❛ ᑭσɳց ❜!__**")
    end = datetime.now()
    ms = (end - start).microseconds / 1000
    if REBEL_IMG:
        REBEL_caption = f"╰•★★  ℘ơŋɠ ★★•╯\n\n    ⚘  `{ms}`\n    ⚘  Oɯɳҽɾ [{DEFAULTUSER}](tg://user?id={REBELOP})"
        await event.client.send_file(event.chat_id, REBEL_IMG, caption=REBEL_caption)
        await event.delete()


CmdHelp("ping").add_command(
    "ping", None, "Shows you the ping speed of server"
).add()
