import os
import logging
from logging.handlers import RotatingFileHandler




TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "7259590228:AAEKoANUwZUuvd8FUVyOQ3Cbxe_49H32vlo")
APP_ID = int(os.environ.get("APP_ID", "16575077"))
API_HASH = os.environ.get("API_HASH", "1c8c0bcb55c14e0fd8078058966b6a11")


OWNER = os.environ.get("OWNER", "@") #Owner username
OWNER_ID = int(os.environ.get("OWNER_ID", "1702061654")) #Owner user id
DB_URL = os.environ.get("DB_URL", "mongodb+srv://madarazbotz:O8WtNAEReh6ohJEt@cluster0.9mosuuk.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DB_NAME = os.environ.get("DB_NAME", "pomoibot")


CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002213043042"))
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "-1001757250028"))


SECONDS = int(os.getenv("SECONDS", "600")) # auto delete in seconds



PORT = os.environ.get("PORT", "8080")
TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))




START_MSG = os.environ.get("START_MESSAGE", "<b> Hᴇʟʟᴏ {first}🙌\n\nI ᴀᴍ ᴀ Fɪʟᴇ [ᴍᴏᴠɪᴇ/ꜱᴇʀɪᴇꜱ/ᴀɴɪᴍᴇ] Pʀᴏᴠɪᴅᴇʀ ʙᴏᴛ \nSᴜʙꜱᴄʀɪʙᴇ ᴛᴏ ᴍʏ Cʜᴀɴɴᴇʟ ᴛᴏ ɢᴇᴛ Fɪʟᴇꜱ ☠️\n\nMᴏᴠɪᴇ/Sᴇʀɪᴇꜱ ~ <a href='https://t.me/+g2ccWFbI2XJkMTE9'>Jᴏɪɴ Hᴇʀᴇ</a>\n\nPᴏᴡᴇʀᴇᴅ ʙʏ <a href='https://t.me/BinaryQuest'>Bɪɴᴀʀʏ Qᴜᴇꜱᴛ 🖤</a></b>")

try:
    ADMINS=[7085541484]
    for x in (os.environ.get("ADMINS", "1844080002 1663603208").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")


FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "Hello {first}\n\n<b>You need to join in my Channel/Group to use me\n\nKindly Please join : <a href='https://t.me/+g2ccWFbI2XJkMTE9'>Cʟɪᴄᴋ Mᴇ 🖤</a></b>")

CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "True" else False

DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True'

BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "<b>Tʜᴀɴᴋ Yᴏᴜ ꜰᴏʀ ᴜꜱɪɴɢ Oᴜʀ ʙᴏᴛ..!\n\nPʟᴇᴀꜱᴇ Jᴏɪɴ - <a href='https://t.me/+g2ccWFbI2XJkMTE9'>Lᴀᴛᴇꜱᴛ Mᴏᴠɪᴇꜱ 🔥</a>\n\nTᴏ ɢᴇᴛ Aʟʟ ʟᴀᴛᴇꜱᴛ Mᴏᴠɪᴇ/Sᴇʀɪᴇꜱ 🖤</b>"

ADMINS.append(OWNER_ID)
ADMINS.append(7085541484)

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
   
