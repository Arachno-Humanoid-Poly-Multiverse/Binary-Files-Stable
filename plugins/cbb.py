from pyrogram import __version__
from bot import Bot
from config import START_MSG, OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from pyrogram import filters
import psutil
import time
from datetime import datetime
from helper_func import get_readable_time

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text=f"<b>○ 🖤 ᴍʏ ᴄʀᴇᴀᴛᴏʀ : <a href='https://t.me/BinaryQuest'>BɪɴᴀʀʏQᴜᴇꜱᴛ</a> \n○ ❤️‍🔥 ꜱᴜᴘᴘᴏʀᴛ : @BQChats \n○ 🔥Library : <a href='https://docs.pyrogram.org/'>Pyrogram asyncio {__version__}</a>\n○ 🥶sᴏᴜʀᴄᴇ ᴄᴏᴅᴇ  : <a href='https://t.me/itz_sahil_official'>ᴘʀɪᴠᴀᴛᴇ ᴄᴏᴅᴇ</a>\n○ 🥵 ᴅᴏɴᴀᴛᴇ ᴍᴇ : <a href='https://t.me/itz_sahil_official/52'>ᴄʟɪᴄᴋ ᴍᴇ</a></b>",
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("🔙 ʙᴀᴄᴋ", callback_data="start"),
                        InlineKeyboardButton("ᴅᴏɴᴀᴛᴇ 🥰", callback_data="donate")
                    ],
                    [
                        InlineKeyboardButton("ᴄʟᴏsᴇ ᴍᴇ 🥀", callback_data="close")
                    ]
                ]
            )
        )
    elif data == "donate":
        await query.message.edit_text(
            text="""
<b>❤️ᴛʜᴀɴᴋs ꜰᴏʀ sʜᴏᴡɪɴɢ ɪɴᴛᴇʀᴇsᴛ ɪɴ ᴅᴏɴᴀᴛɪᴏɴ 😟

ᴅᴏɴᴀᴛᴇ ᴜs ᴛᴏ ᴋᴇᴇᴘ ᴏᴜʀ sᴇʀᴠɪᴄᴇs ᴄᴏɴᴛɪɴᴏᴜsʟʏ ᴀʟɪᴠᴇ 😢
ʏᴏᴜ ᴄᴀɴ sᴇɴᴅ ᴀɴʏ ᴀᴍᴏᴜɴᴛ 
ᴏꜰ 10₹, 20₹, 30₹, 50₹, 70₹, 100₹, 200₹ ...ᴀs ʏᴏᴜ ᴡɪsʜ 😊

📨 ᴘᴀʏᴍᴇɴᴛ ᴍᴇᴛʜᴏᴅs 💳

ɢᴏᴏɢʟᴇᴘᴀʏ / ᴘᴀʏᴛᴍ / ᴘʜᴏɴᴘᴀʏ / ɴᴇᴛ ʙᴀɴᴋɪɴɢ ... 

❤️ꜰᴏʀ ᴅᴏɴᴀᴛɪᴏɴ ᴍᴇssᴀɢᴇ ᴍᴇ💬 
 👉Cʟɪᴄᴋ Hᴇʀᴇ (https://t.me/BinaryQuest/79) [or here via this bot]

ᴏʀ ʏᴏᴜ ᴄᴀɴ sᴄᴀɴ ᴛʜᴇ ǫʀ ᴄᴏᴅᴇ 👇
ᴜᴘɪ ʟɪɴᴋ 🔗 ᴀʟsᴏ ᴛʜᴇʀᴇ 😇
🌹 ᴛʜᴀɴᴋɪɴɢ ʏᴏᴜ 🌹</b>
            """,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("ᴀʙᴏᴜᴛ", callback_data="about"),
                        InlineKeyboardButton("ᴄʟᴏsᴇ ᴍᴇ 🥀", callback_data="close")
                    ]
                ]
            )
        )
    elif data == "start":
        user = query.from_user
        await query.message.edit_text(
            text=START_MSG.format(
                first=user.first_name,
                last=user.last_name or "",
                username=f"@{user.username}" if user.username else "No Username",
                mention=user.mention,
                id=user.id
            ),
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("❤️‍🔥 ᴍʏ ᴄʀᴇᴀᴛᴏʀ 🥵", callback_data="about"),
                        InlineKeyboardButton("🥺 ᴄʟᴏsᴇ ᴍᴇ 🌟", callback_data="close")
                    ]
                ]
            )
        )
    elif data == "stats":
        now = datetime.now()
        delta = now - client.uptime
        uptime = get_readable_time(delta.seconds)
        cpu = psutil.cpu_percent(interval=0.5)
        mem = psutil.virtual_memory().percent
        disk = psutil.disk_usage("/").percent
        text = f"""
𝙎𝙮𝙨𝙩𝙚𝙢 𝙨𝙩𝙖𝙩𝙨
➖➖➖➖➖➖
UPTIME ➼ {uptime}
CPU ➼ {cpu}%
RAM ➼ {mem}%
DISK ➼ {disk}%

PYTHON ➼ 3.11.9

PTB ➼ 21.4
TELETHON ➼ 1.36.0
PYROGRAM ➼ 2.0.106
"""
        await query.answer(text=text, show_alert=True)
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass
