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
        print("π°π΄π½κͺπ³π½ βππ§π°π₯π―π’π’π°")
        bot.loop.run_until_complete(add_bot(Var.TG_BOT_USER_NAME_BF_HER))
        print("β‘αα©αΥαΌαα΄α΄ ΥTα©αTαα­ αOα°α­αͺα΄Tα΄αͺβ‘")
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
    f"""πππ°ππ ππΎππ π±πΎπ π½πΎπ π²π·π΄π²πΊ [.alive/.ping] ππ΄πππΈπΎπ½ :-{REBELversion}."""
)

if len(argv) not in (1, 3, 4):
    bot.disconnect()
else:
    bot.run_until_disconnected()
