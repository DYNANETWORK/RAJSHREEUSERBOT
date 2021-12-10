import os
from pathlib import Path
from sys import argv

import telethon.utils
from telethon import TelegramClient

from userbot import REBELversion, bot
from userbot.utils import load_module
from var import Var

os.system("pip install -U telethon")


async def add_bot(bot_token):
    await bot.start(bot_token)
    bot.me = await bot.get_me()
    bot.uid = telethon.utils.get_peer_id(bot.me)


if len(argv) not in (1, 3, 4):
    bot.disconnect()
else:
    bot.tgbot = None
    if Var.TG_BOT_USER_NAME_BF_HER is not None:
        print("Initiating Inline Bot")
        # ForTheGreatrerGood of beautification
        bot.tgbot = TelegramClient(
            "TG_BOT_TOKEN", api_id=Var.APP_ID, api_hash=Var.API_HASH
        ).start(bot_token=Var.TG_BOT_TOKEN_BF_HER)
        print("Initialisation finished with no errors")
        print("🔰𝘴𝓽ꪖ𝘳𝓽 ℜ𝔞𝔧𝔰𝔥𝔯𝔢𝔢🔰")
        bot.loop.run_until_complete(add_bot(Var.TG_BOT_USER_NAME_BF_HER))
        print("⚡ᖇᗩᒍՏᕼᖇᗴᗴ ՏTᗩᖇTᑌᑭ ᑕOᗰᑭᒪᗴTᗴᗪ⚡")
    else:
        bot.start()


import glob

path = "userbot/plugins/*.py"
files = glob.glob(path)
for name in files:
    with open(name) as f:
        path1 = Path(f.name)
        shortname = path1.stem
        load_module(shortname.replace(".py", ""))


print(
    f"""𝚂𝚃𝙰𝚁𝚃 𝚈𝙾𝚄𝚁 𝙱𝙾𝚃 𝙽𝙾𝚆 𝙲𝙷𝙴𝙲𝙺 [.alive/.ping] 𝚅𝙴𝚁𝚂𝙸𝙾𝙽 :-{REBELversion}."""
)

if len(argv) not in (1, 3, 4):
    bot.disconnect()
else:
    bot.run_until_disconnected()
