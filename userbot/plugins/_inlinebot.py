
# Help Pic feature added by πππππ πππππ = @H1M4N5HU0P


from math import ceil
from re import compile

from REBELBOT.utils import *
from telethon.events import InlineQuery, callbackquery
from telethon.sync import custom

from userbot import *
from userbot.cmdhelp import *
from userbot.Config import Config


REBEL_row = Config.BUTTONS_IN_HELP
REBEL_emoji = Config.EMOJI_IN_HELP

def button(page, modules):
    Row = REBEL_row

    modules = sorted([modul for modul in modules if not modul.startswith("_")])
    pairs = list(map(list, zip(modules[::2], modules[1::2])))
    if len(modules) % 2 == 1:
        pairs.append([modules[-1]])
    max_pages = ceil(len(pairs) / Row)
    pairs = [pairs[i : i + Row] for i in range(0, len(pairs), Row)]
    buttons = []
    for pairs in pairs[page]:
        buttons.append(
            [
                custom.Button.inline(
                    f"{REBEL_emoji} " + pair, data=f"Information[{page}]({pair})"
                )
                for pair in pairs
            ]
        )

    buttons.append(
        [
            custom.Button.inline(
                f"βοΈ α°α―α£α¦ {REBEL_emoji}",
                data=f"page({(max_pages - 1) if page == 0 else (page - 1)})",
            ),
            custom.Button.inline(f"β’{REBEL_emoji} β {REBEL_emoji}β’", data="close"),
            custom.Button.inline(
                f"{REBEL_emoji} ααοΎαΏ βΆοΈ",
                data=f"page({0 if page == (max_pages - 1) else page + 1})",
            ),
        ]
    )
    return [max_pages, buttons]
    # Changing this line may give error in bot as i added some special cmds in REBELBOT channel to get this module work...

    modules = CMD_HELP


if Var.TG_BOT_USER_NAME_BF_HER is not None and tgbot is not None:

    @tgbot.on(InlineQuery)  # pylint:disable=E0602
    async def inline_handler(event):
        builder = event.builder
        result = None
        query = event.text
        if event.query.user_id == bot.uid and query == "@REBELBOT_SUPPORT":
            rev_text = query[::-1]
            veriler = button(0, sorted(CMD_HELP))
            result = await builder.article(
                f"Hey! Only use .help please",
                text=f"**Running βππ§π°π₯π―π’π’**\n\n__Number of plugins installed__ :`{len(CMD_HELP)}`\n**page:** 1/{veriler[0]}",
                buttons=veriler[1],
                link_preview=True,
            )
        elif query.startswith("http"):
            part = query.split(" ")
            result = builder.article(
                "File uploaded",
                text=f"**File uploaded successfully to {part[2]} site.\n\nUpload Time : {part[1][:3]} second\n[βββ β]({part[0]})",
                buttons=[[custom.Button.url("URL", part[0])]],
                link_preview=True,
            )
        elif event.text == "":
            result = builder.article(
                "@REBELBOT_SUPPORT",
                text=f"""**Hey! This is [βππ§π°π₯π―π’π’](https://t.me/rashreesupport)\nYou can know more about me from the links given below π**""",
                buttons=[
                    [
                        custom.Button.url(
                            "π₯ CHANNEL π₯", "https://t.me/rashreesupport"
                        ),
                        custom.Button.url(
                            "β‘ GROUP β‘", "https://t.me/rashreesupport"
                        ),
                    ],
                    [
                        custom.Button.url(
                            "π° REPO π°", "https://github.com/REBEL75/REBELBOTOP"
                        ),
                        custom.Button.url("π° TUTORIAL π°", ""),
                    ],
                ],
                link_preview=True,
            )
        await event.answer([result] if result else None)

    @tgbot.on(callbackquery.CallbackQuery(data=compile(b"page\((.+?)\)")))
    async def page(event):
        if not event.query.user_id == bot.uid:
            return await event.answer(
                "HELLO THERE. PLEASE MAKE YOUR OWN βππ§π°π₯π―π’π’ AND USE. Β©βππ§π°π₯π―π’π’ β’",
                cache_time=0,
                alert=True,
            )
        page = int(event.data_match.group(1).decode("UTF-8"))
        veriler = button(page, CMD_HELP)
        await event.edit(
            f"**Legenday AF [βππ§π°π₯π―π’π’ π€](https://t.me/rashreesupport) __Working...__\n\n**Number of modules installed :** `{len(CMD_HELP)}`\n**page:** {page + 1}/{veriler[0]}",
            buttons=veriler[1],
            link_preview=True,
        )

    @tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"close")))
    async def on_plug_in_callback_query_handler(event):
        if event.query.user_id == bot.uid:
            await delete_REBEL(
                event,
                f"βοΈβππ§π°π₯π―π’π’ Menu Provider Is now ClosedβοΈ\n\n         **[Β©βππ§π°π₯π―π’π’ β’](t.me/rashreesupport)**[β‘π₯]({REBEL_help_pic})",
                5,
                link_preview=True,
            )
        else:
            REBEL_alert = (
                "HELLO THERE. PLEASE MAKE YOUR OWN βππ§π°π₯π―π’π’ AND USE. Β©βππ§π°π₯π―π’π’ β’"
            )
            await event.answer(REBEL_alert, cache_time=0, alert=True)

    @tgbot.on(
        callbackquery.CallbackQuery(data=compile(b"Information\[(\d*)\]\((.*)\)"))
    )
    async def Information(event):
        if not event.query.user_id == bot.uid:
            return await event.answer(
                "HELLO THERE. PLEASE MAKE YOUR OWN βππ§π°π₯π―π’π’ AND USE. Β©βππ§π°π₯π―π’π’ β’",
                cache_time=0,
                alert=True,
            )

        page = int(event.data_match.group(1).decode("UTF-8"))
        commands = event.data_match.group(2).decode("UTF-8")
        try:
            buttons = [
                custom.Button.inline(
                    "π·" + cmd[0], data=f"commands[{commands}[{page}]]({cmd[0]})"
                )
                for cmd in CMD_HELP_BOT[commands]["commands"].items()
            ]
        except KeyError:
            return await event.answer(
                "No Description is written for this plugin", cache_time=0, alert=True
            )

        buttons = [buttons[i : i + 2] for i in range(0, len(buttons), 2)]
        buttons.append([custom.Button.inline("βοΈ α°α―α£α¦", data=f"page({page})")])
        await event.edit(
            f"**π File:** `{commands}`\n**π’ Number of commands :** `{len(CMD_HELP_BOT[commands]['commands'])}`",
            buttons=buttons,
            link_preview=False,
        )

    @tgbot.on(
        callbackquery.CallbackQuery(data=compile(b"commands\[(.*)\[(\d*)\]\]\((.*)\)"))
    )
    async def commands(event):
        if not event.query.user_id == bot.uid:
            return await event.answer(
                "HELLO THERE. PLEASE MAKE YOUR OWN βππ§π°π₯π―π’π’ AND USE. Β©βππ§π°π₯π―π’π’ β’",
                cache_time=0,
                alert=True,
            )

        cmd = event.data_match.group(1).decode("UTF-8")
        page = int(event.data_match.group(2).decode("UTF-8"))
        commands = event.data_match.group(3).decode("UTF-8")

        result = f"**π File:** `{cmd}`\n"
        if CMD_HELP_BOT[cmd]["info"]["info"] == "":
            if not CMD_HELP_BOT[cmd]["info"]["warning"] == "":
                result += f"**β¬οΈ Official:** {'β' if CMD_HELP_BOT[cmd]['info']['official'] else 'β'}\n"
                result += f"**β οΈ Warning :** {CMD_HELP_BOT[cmd]['info']['warning']}\n\n"
            else:
                result += f"**β¬οΈ Official:** {'β' if CMD_HELP_BOT[cmd]['info']['official'] else 'β'}\n\n"
        else:
            result += f"**β¬οΈ Official:** {'β' if CMD_HELP_BOT[cmd]['info']['official'] else 'β'}\n"
            if not CMD_HELP_BOT[cmd]["info"]["warning"] == "":
                result += f"**β οΈ Warning:** {CMD_HELP_BOT[cmd]['info']['warning']}\n"
            result += f"**βΉοΈ Info:** {CMD_HELP_BOT[cmd]['info']['info']}\n\n"

        command = CMD_HELP_BOT[cmd]["commands"][commands]
        if command["params"] is None:
            result += f"**π  Commands:** `{COMMAND_HAND_LER[:1]}{command['command']}`\n"
        else:
            result += f"**π  Commands:** `{COMMAND_HAND_LER[:1]}{command['command']} {command['params']}`\n"

        if command["example"] is None:
            result += f"**π¬ Explanation:** `{command['usage']}`\n\n"
        else:
            result += f"**π¬ Explanation:** `{command['usage']}`\n"
            result += (
                f"**β¨οΈ For Example:** `{COMMAND_HAND_LER[:1]}{command['example']}`\n\n"
            )

        await event.edit(
            result,
            buttons=[
                custom.Button.inline("βοΈ α°α―α£α¦", data=f"Information[{page}]({cmd})")
            ],
            link_preview=False,
        )


# Ask owner before using it in your codes
# Kangers like LB stay away...
