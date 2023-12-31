from typing import Union

from pyrogram.types import InlineKeyboardButton

import config
from AnonX import app


def start_pannel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="🌷𝐀ԃ𝐃 𝐌ҽ 𝐓σ 𝐘συ𝐑 𝐆ɾσυ𝐏🌷",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text="𝐂σɱɱαɳԃ𝐒",
                callback_data="settings_back_helper",
            ),
            InlineKeyboardButton(
                text="𝐒ҽƚƚιɳɠ𝐒", callback_data="settings_helper"
            ),
        ],
        [
            InlineKeyboardButton(
                text="𝐅συɳԃҽ𝐑", user_id=OWNER),
            InlineKeyboardButton(
                text="𝐆ɾσυ𝐏", url=f"{config.SUPPORT_GROUP}"
            ),
        ],
     ]
    return buttons


def private_panel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="🌷𝐀ԃ𝐃 𝐌ҽ 𝐓σ 𝐘συ𝐑 𝐆ɾσυ𝐏🌷",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            ),
        ],
        [
            InlineKeyboardButton(
                text="𝐂σɱɱαɳԃ𝐒", callback_data="settings_back_helper"
            ),
        ],
        [
            InlineKeyboardButton(text="ᴍᴀɪɴᴛᴀɪɴᴇʀ", user_id=OWNER),
            InlineKeyboardButton(
                text="𝐆ɾσυ𝐏", url=f"{config.SUPPORT_GROUP}"
            ),
        ],
        [
            InlineKeyboardButton(
                    text="🌹 𝑀𝑦𝑟𝑎 network 🌹", url="https://t.me/myra_updates"
                )
        ],
     ]
    return buttons
