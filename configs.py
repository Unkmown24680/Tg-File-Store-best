# (c) @PredatorHackerzZ || @TeleRoidGroup

import os


class Config(object):
	API_ID = int(os.environ.get("API_ID", "23576751"))
	API_HASH = os.environ.get("API_HASH", "5224da0df5c60ec53de09ce79b9aa2c3")
	BOT_TOKEN = os.environ.get("BOT_TOKEN","6943972205:AAEVgI7yUdPuNieqe6OLPUvIvDegAVTFN1c")
	BOT_USERNAME = os.environ.get("BOT_USERNAME","file_store_bmw_bot")
	DB_CHANNEL = int(os.environ.get("DB_CHANNEL", "-1001960613454"))
	BOT_OWNER = int(os.environ.get("BOT_OWNER", "1720819569"))
	DATABASE_URL = os.environ.get("DATABASE_URL","mongodb+srv://dohoj11515:f5VibAbQ4LVHpQ5n@cluster0.h3s7s7p.mongodb.net/?retryWrites=true&w=majority")
	UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", "1907166812")
	LOG_CHANNEL = os.environ.get("LOG_CHANNEL", "2088041233")
	BANNED_USERS = set(int(x) for x in os.environ.get("BANNED_USERS", "1234567890").split())
	FORWARD_AS_COPY = bool(os.environ.get("FORWARD_AS_COPY", True))
	BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", False))
	BANNED_CHAT_IDS = list(set(int(x) for x in os.environ.get("BANNED_CHAT_IDS", "").split()))
	OTHER_USERS_CAN_SAVE_FILE = bool(os.environ.get("OTHER_USERS_CAN_SAVE_FILE", True))
	ABOUT_BOT_TEXT = f"""
This is a Permanent FileStore Bot. 
Send Me any Media or File.I can Work In Channel too Add Me to Channel with Edit Permission, I will add save Uploaded File in Channel and Share a Shareable Link. 

╭────[ **🔅FɪʟᴇSᴛᴏʀᴇBᴏᴛ🔅**]────⍟
│
├🔸🤖 **My Name:** [𝐅𝐢𝐥𝐞 𝐒𝐭𝐨𝐫𝐞 𝐁𝐨𝐭](https://t.me/{BOT_USERNAME})
│
├🔸📝 **Language:** [𝐏𝐲𝐭𝐡𝐨𝐧𝟑](https://www.python.org)
│
├🔹📚 **Library:** [𝐏𝐲𝐫𝐨𝐠𝐫𝐚𝐦](https://docs.pyrogram.org)
│
├🔹📡 **Hosted On:** [𝐇𝐞𝐫𝐨𝐤𝐮](https://heroku.com)
│
├🔸👨‍💻 **Developer:** [@Movierulzking](https://t.me/movierulzking) 
│
├🔹👥 **Support:** [𝐒𝐮𝐩𝐩𝐨𝐫𝐭](https://t.me/hotflashdealss)
│
├🔸🔔 **Movie Group:** [𝐔𝐩𝐝𝐚𝐭𝐞𝐬](https://t.me/requestyourmoviehere)
│
╰──────[ 😎 ]───────────⍟
"""
	ABOUT_DEV_TEXT = f"""
🧑🏻‍💻 **Main Channel:** [@Movierulzking](https://t.me/movierulzking) 

 **Any Queries :** [Contact me](https://t.me/sm_contactadmin_bot) 
"""
	HOME_TEXT = """
Hello, [{}](tg://user?id={})\n\nThis is a Permanent **FileStore Bot**.

How to Use Bot??

📢 Send me any File & It will be uploaded in My Database & You will Get the File Link.

I can also work in channel Just add me in your channel as admin.

"""
