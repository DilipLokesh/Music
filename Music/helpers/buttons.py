from pyrogram.types import InlineKeyboardButton

from Music.core.clients import hellbot


class MakeButtons:
    def close_markup():
        buttons = [[InlineKeyboardButton("🗑", callback_data="close")]]
        return buttons

    def player_markup(chat_id, video_id):
        buttons = [
            [
                InlineKeyboardButton("About Song", url=f"https://t.me/{hellbot.app.username}?start=song_{video_id}"),
            ],
            [
                InlineKeyboardButton("❤️", callback_data=f"add_favorite|{video_id}"),
                InlineKeyboardButton("🎛️", callback_data=f"controls|{chat_id}|{video_id}"),
            ],
            [
                InlineKeyboardButton("🗑", callback_data="close"),
            ],
        ]
        return buttons

    def controls_markup(video_id, chat_id):
        buttons = [
            [
                InlineKeyboardButton(text="⟲", callback_data=f"authcontrols|bseek|{chat_id}"),
                InlineKeyboardButton(text="⦿", callback_data=f"authcontrols|play|{chat_id}"),
                InlineKeyboardButton(text="⟳", callback_data=f"authcontrols|fseek|{chat_id}"),
            ],
            [
                InlineKeyboardButton(text="⊡ End", callback_data=f"authcontrols|end|{chat_id}"),
                InlineKeyboardButton(text="↻ Replay", callback_data=f"authcontrols|replay|{chat_id}"),
                InlineKeyboardButton(text="∞ Loop", callback_data=f"authcontrols|loop|{chat_id}"),
            ],
            [
                InlineKeyboardButton(text="⊝ Mute", callback_data=f"authcontrols|mute|{chat_id}"),
                InlineKeyboardButton(text="⊜ Unmute", callback_data=f"authcontrols|unmute|{chat_id}"),
                InlineKeyboardButton(text="⊹ Skip", callback_data=f"authcontrols|skip|{chat_id}"),
            ],
            [
                InlineKeyboardButton(text="🔙", callback_data=f"controls|{chat_id}|{video_id}"),
                InlineKeyboardButton(text="🗑", callback_data="close"),
            ]
        ]
        return buttons

    def song_markup(rand_key, url, key):
        buttons = [
            [
                InlineKeyboardButton(text="Visit Youtube", url=url),
            ],
            [
                InlineKeyboardButton(text="Audio", callback_data=f"song_dl|adl|{key}|{rand_key}"),
                InlineKeyboardButton(text="Video", callback_data=f"song_dl|vdl|{key}|{rand_key}"),
            ],
            [
                InlineKeyboardButton(text="⪨", callback_data=f"song_dl|prev|{key}|{rand_key}"),
                InlineKeyboardButton(text="⪩", callback_data=f"song_dl|next|{key}|{rand_key}"),
            ],
            [
                InlineKeyboardButton(text="🗑", callback_data=f"song_dl|close|{key}|{rand_key}"),
            ],
        ]
        return buttons

    def song_details_markup(videoid, url, ch_url):
        buttons = [
            [
                InlineKeyboardButton(text="📝 Description", callback_data=f"about_song|desc|{videoid}"),
            ],
            [
                InlineKeyboardButton(text="🎥", url=url),
                InlineKeyboardButton(text="📺", url=ch_url),
            ],
            [
                InlineKeyboardButton(text="🗑", callback_data="close"),
            ]
        ]
        return buttons

    def help_gc_markup():
        buttons = [
            [
                InlineKeyboardButton(text="Get Help ❓", url=f"https://t.me/{hellbot.app.username}?start=help"),
                InlineKeyboardButton(text="🗑", callback_data="close"),
            ]
        ]
        return buttons

    def help_pm_markup():
        buttons = [
            [
                InlineKeyboardButton(text="➊ Admins", callback_data="help|admin"),
                InlineKeyboardButton(text="➋ Users", callback_data="help|user"),
            ],
            [
                InlineKeyboardButton(text="➌ Sudos", callback_data="help|sudo"),
                InlineKeyboardButton(text="➍ Others", callback_data="help|others"),
            ]
            [
                InlineKeyboardButton(text="🗑", callback_data="close"),
            ]
        ]
        return buttons