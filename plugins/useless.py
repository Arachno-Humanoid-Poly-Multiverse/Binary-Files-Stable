# Jishu Developer 
# Don't Remove Credit 🥺
# Telegram Channel @Madflix_Bots
# Backup Channel @JishuBotz
# Developer @JishuDeveloper




from bot import Bot
from pyrogram.types import Message
from pyrogram import filters
from config import ADMINS, BOT_STATS_TEXT, USER_REPLY_TEXT
from datetime import datetime
from helper_func import get_readable_time
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery


@Bot.on_message(filters.command('stats'))
async def stats(bot: Bot, message: Message):
    keyboard = InlineKeyboardMarkup(
        [
            [InlineKeyboardButton("View Stats", callback_data="stats")],
            [InlineKeyboardButton("Close Me", callback_data="close")]
        ]
    )
    picture_url = "https://telegra.ph/file/ea2ee79f2c74f287e5bc0.jpg"
    caption_text = "ᴀʜʜʜ! 🎀 ᴡᴀɴɴᴀ ᴄʜᴇᴄᴋ ᴍʏ ᴄᴀᴘᴀᴄɪᴛʏ ?"

    await bot.send_photo(
        chat_id=message.chat.id,
        photo=picture_url,
        caption=caption_text,
        reply_markup=keyboard
    )



@Bot.on_message(filters.private & filters.incoming)
async def useless(_,message: Message):
    if USER_REPLY_TEXT:
        await message.reply(USER_REPLY_TEXT)





# Jishu Developer 
# Don't Remove Credit 🥺
# Telegram Channel @Madflix_Bots
# Backup Channel @JishuBotz
# Developer @JishuDeveloper
