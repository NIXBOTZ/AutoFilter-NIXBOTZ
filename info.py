import re
from os import environ,getenv
from Script import script

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default
        
#-------------------------- ʙoᴛ sᴇᴛᴛɪɴɢs --------------------------

CACHE_TIME = int(environ.get('CACHE_TIME', 300))
USE_CAPTION_FILTER = bool(environ.get('USE_CAPTION_FILTER', True))

#------------------------- ʙoᴛ ɪɴғoʀᴍᴀᴛɪᴏɴ --------------------------

SESSION = environ.get('SESSION', 'NIXBOTZ')
API_ID = int(environ.get('API_ID', ''))
API_HASH = environ.get('API_HASH', '')
BOT_TOKEN = environ.get('BOT_TOKEN', "")

#--------------------------- ɪᴍᴀɢᴇs ʟɪɴᴋ -----------------------------

# sᴛᴀʀᴛ ɪᴍᴀɢᴇs ʟɪɴᴋ  || ʏoᴜ cᴀɴ ᴀᴅᴅ ᴍᴜʟᴛɪᴘʟᴇꜱ ɪᴍᴀɢᴇs ʟɪɴᴋ ʙʏ ɢɪvɪɴɢ oɴᴇ sᴘᴀcᴇ ʙᴇᴛwᴇᴇɴ ᴇᴀc𝙷
PICS = (environ.get('PICS', 'https://graph.org/file/5e1f8888547a1a896a902.jpg https://graph.org/file/9649c1dcbae09f2e7700e.jpg')).split() 

NOR_IMG = environ.get("NOR_IMG", "https://graph.org/file/549fd9f3272214acade82.jpg")
MELCOW_VID = environ.get("MELCOW_VID", "https://graph.org/file/ccf3cbc4687263ac63420.jpg")
SPELL_IMG = environ.get("SPELL_IMG", "https://graph.org/file/549fd9f3272214acade82.jpg")

FORCESUB_IMG = (environ.get('FORCESUB_IMG', 'https://graph.org/file/9649c1dcbae09f2e7700e.jpg'))

REFER_IMG = (environ.get("REFER_IMG", "https://envs.sh/PSI.jpg")).split() 

SUBSCRIPTION = (environ.get('SUBSCRIPTION', 'https://graph.org/file/347c1f79f36d3cf14e0f5.jpg'))
CODE = (environ.get('CODE', 'https://graph.org/file/02e7ecc3e2693b481b914.jpg'))

#------------------ sᴛᴀʀᴛ ᴄᴏᴍᴍᴀɴᴅ ʀᴇᴀcᴛɪoɴs ----------------------

REACTIONS = ["🦋",, "🤝", "😇", "🤗", "😍", "😎",  "👍", "🌚", "🎅", "😁", "😐", "🥰", "🤩", "😈", "😱", "🤣", "😘", "👏", "😛", "🎉", "⚡️", "🫡", "🤓", "🏆", "🔥", "🤭", "🆒", "👻"] # ᴅoɴ'ᴛ ᴀᴅᴅ ᴀɴʏ ᴇᴍojɪ ʙᴇcᴀᴜsᴇ ᴛɢ ɴᴏᴛ sᴜᴘᴘoʀᴛ ᴀʟʟ ᴇᴍojɪ

#-------------------------- ʀᴇғᴇʀᴀʟ sᴇᴛᴛɪɴɢs -------------------------

REFERAL_COUNT = int(environ.get('REFERAL_COUNT', '20')) # ɴᴜᴍʙᴇʀ ᴏꜰ ʀᴇғᴇʀᴀʟ coᴜɴᴛ
REFERAL_PREMEIUM_TIME = environ.get('REFERAL_PREMEIUM_TIME', '1 week') 
OWNER_USERNAME = environ.get('OWNER_USERNAME', 'IM_NISHANTT') # owɴᴇʀ ᴜsᴇʀɴᴀᴍᴇ wɪᴛʜoᴜᴛ @ 

#-------------------------------- ɪᴅ -----------------------------------

# 📌 ɴoᴛᴇ: ɢɪvᴇ ʙᴇʟow vᴀʀɪᴀʙʟᴇs wʜo cʜᴀɴɴᴇʟs ɪᴅ ᴀᴅᴅ ɪɴ ᴛʜᴇ cʜᴀɴɴᴇʟ, ʙᴏᴛ ᴍᴜsᴛ ᴀᴅᴍɪɴ wɪᴛʜ ꜰᴜʟʟ sᴜᴘᴘoʀᴛ

# ᴀᴅᴍɪɴs ɪᴅ  || ɪꜰ ʏoᴜ ꜰɪʟʟ ᴍᴜʟᴛɪᴘʟᴇꜱ ɪᴅ ꜰ ʙʏ ɢɪvɪɴɢ oɴᴇ sᴘᴀcᴇ ʙᴇᴛwᴇᴇɴ ᴇᴀc𝙷 ʟɪᴋᴇ
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '6899946963').split()]

# ɢɪvᴇ wʜo cʜᴀɴɴᴇʟ ɪᴅ wʜᴇʀᴇ ʏoᴜ ᴜᴘʟoᴀᴅ ʏoᴜʀ ꜰɪʟᴇꜱ ᴛʜᴇɴ, ʙᴏᴛ ᴀᴜᴛoᴍᴀᴛɪcᴀʟʟʏ sᴀvᴇ ɪᴛ ɪɴ ᴅᴀᴛᴀʙᴀsᴇ. ɪᴛ ɪs ᴀʟso ᴋɴowɴ ᴀs ꜰɪʟᴇ cʜᴀɴɴᴇʟ.
CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ.get('CHANNELS', '').split()]

# ɢɪvᴇ wʜo cʜᴀɴɴᴇʟ ɪᴅ wʜᴇʀᴇ ʙᴏᴛ sᴇɴᴅ ᴍᴇꜱꜱᴀɢᴇs ɪꜰ ɴᴇw ᴜsᴇʀ sᴛᴀʀᴛ ᴛʜᴇ ʙᴏᴛ ᴏʀ ʙᴏᴛ sᴇɴᴅ ꜰɪʟᴇꜱ ᴀɴʏ ᴜsᴇʀ.
LOG_CHANNEL = int(environ.get('LOG_CHANNEL', ''))

# ɢɪvᴇ wʜo cʜᴀɴɴᴇʟ ɪᴅ wʜᴇʀᴇ ʙᴏᴛ oɴʟʏ sᴇɴᴅ ᴘʀᴇᴍɪᴜᴍ ᴍᴇꜱꜱᴀɢᴇs 
PREMIUM_LOGS = int(environ.get('PREMIUM_LOGS', '')) 

# ɢɪvᴇ wʜo cʜᴀɴɴᴇʟ ɪᴅ wʜᴇʀᴇ ʙᴏᴛ ᴅᴇʟᴇᴛᴇ ɪɴᴅᴇx ꜰɪʟᴇ, ғoʀwᴀʀᴅ wʜo ꜰɪʟᴇ ɪɴ ᴛʜᴇ cʜᴀɴɴᴇʟ ғʀoᴍ ꜰɪʟᴇ cʜᴀɴɴᴇʟ wʜɪcʜ ʏoᴜ wᴀɴᴛ ᴛo ᴅᴇʟᴇᴛᴇ ᴛʜᴇɴ, ʙᴏᴛ ᴀᴜᴛoᴍᴀᴛɪcᴀʟʟʏ ᴅᴇʟᴇᴛᴇ ᴛʜᴀᴛ ꜰɪʟᴇ ғʀoᴍ ᴅᴀᴛᴀʙᴀsᴇ. 
DELETE_CHANNELS = [int(dch) if id_pattern.search(dch) else dch for dch in environ.get('DELETE_CHANNELS', '0').split()]  

auth_users = [int(user) if id_pattern.search(user) else user for user in environ.get('AUTH_USERS', '').split()]
AUTH_USERS = (auth_users + ADMINS) if auth_users else []
PREMIUM_USER = [int(user) if id_pattern.search(user) else user for user in environ.get('PREMIUM_USER', '6899946963').split()]

# ɢɪvᴇ ʏoᴜʀ ғoʀcᴇ sᴜʙscʀɪʙᴇ cʜᴀɴɴᴇʟ ɪᴅ ᴇʟsᴇ ʟᴇᴀvᴇ ɪᴛ ʙʟᴀɴᴋ.
auth_channel = environ.get('AUTH_CHANNEL', '')

# ɢɪvᴇ sᴜᴘᴘoʀᴛ cʜᴀɴɴᴇʟ ɪᴅ ʙᴏᴛ ɴᴏᴛ sᴇɴᴅ ꜰɪʟᴇ ʜᴇʀᴇ ʙᴇcᴀᴜsᴇ ᴛʜɪs ɪs sᴜᴘᴘoʀᴛ cʜᴀɴɴᴇʟ.
support_chat_id = environ.get('SUPPORT_CHAT_ID', '') 

# ɢɪvᴇ wʜo cʜᴀɴɴᴇʟ ɪᴅ ғoʀ ɪꜰ ᴜsᴇʀ ʀᴇQᴜᴇsᴛ ꜰɪʟᴇ wɪᴛʜ ᴄᴏᴍᴍᴀɴᴅ oʀ ʜᴀsʜᴛᴀɢ ʟɪᴋᴇ - /request oʀ #request
reqst_channel = environ.get('REQST_CHANNEL_ID', '') 

# ɢɪvᴇ wʜo cʜᴀɴɴᴇʟ ɪᴅ ғoʀ /batch ᴄᴏᴍᴍᴀɴᴅ ꜰɪʟᴇ sᴛoʀᴇ
FILE_STORE_CHANNEL = [int(ch) for ch in (environ.get('FILE_STORE_CHANNEL', '')).split()]

auth_grp = environ.get('AUTH_GROUP')
AUTH_CHANNEL = int(auth_channel) if auth_channel and id_pattern.search(auth_channel) else None
AUTH_GROUPS = [int(ch) for ch in auth_grp.split()] if auth_grp else None
REQST_CHANNEL = int(reqst_channel) if reqst_channel and id_pattern.search(reqst_channel) else None
SUPPORT_CHAT_ID = int(support_chat_id) if support_chat_id and id_pattern.search(support_chat_id) else None

#------------------------------ ʟɪɴᴋ --------------------------------

GRP_LNK = environ.get('GRP_LNK', 'https://t.me/Ni_Movie_Request_Group') 
CHNL_LNK = environ.get('CHNL_LNK', 'https://t.me/NIXBOTZ') 
SUPPORT_CHAT = environ.get('SUPPORT_CHAT', 'https://t.me/NIXBOTZ_Support') 

#------------------------- ᴍoɴɢoᴅʙ ɪɴꜰᴏʀᴍᴀᴛɪᴏɴ --------------------------------------------

DATABASE_URI = environ.get('DATABASE_URI', "")
DATABASE_NAME = environ.get('DATABASE_NAME', "Cluster0")
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'NIXFILES')

#---------------------------- sʜᴏʀᴛʟɪɴᴋ ---------------------------

SHORTLINK_MODE = is_enabled((environ.get('SHORTLINK_MODE', 'False')), False) # sᴇᴛ True ᴏʀ False
SHORTLINK_API = environ.get('SHORTLINK_API', '') # sᴇᴛ sʜᴏʀᴛʟɪɴᴋ ᴍoᴅᴇ "True" ᴛʜᴇɴ, ᴍᴜsᴛ ғɪʟʟ ᴛʜɪs vᴀʀɪᴀʙʟᴇ !!    
SHORTLINK_URL = environ.get('SHORTLINK_URL', '')  # sᴇᴛ sʜᴏʀᴛʟɪɴᴋ ᴍoᴅᴇ "True" ᴛʜᴇɴ, ᴍᴜsᴛ ᴀʟso ғɪʟʟ ᴛʜɪs vᴀʀɪᴀʙʟᴇ !!    

TUTORIAL = environ.get('TUTORIAL', 'https://t.me/')  # ɢɪvᴇ wʜo cʜᴀɴɴᴇʟ ʟɪɴᴋ wʜᴇʀᴇ ʏoᴜ ᴜᴘʟoᴀᴅ oᴘᴇɴɪɴɢ sʜᴏʀᴛʟɪɴᴋ wᴇʙsɪᴛᴇ

#------------------------------- vᴇʀɪғʏ ---------------------------

VERIFY = bool(environ.get('VERIFY', False)) # sᴇᴛ vᴇʀɪғɪcᴀᴛɪoɴ True ᴏʀ False
VERIFY_SHORTLINK_URL = environ.get('VERIFY_SHORTLINK_URL', '') 

VERIFY_SHORTLINK_API = environ.get('VERIFY_SHORTLINK_API', '')

HOWTOVERIFY = environ.get('HOWTOVERIFY', 'https://t.me/') # ɢɪvᴇ wʜo cʜᴀɴɴᴇʟ ʟɪɴᴋ wʜᴇʀᴇ ʏoᴜ ᴜᴘʟoᴀᴅ ʜow ᴛo vᴇʀɪғʏ vɪᴅᴇo. 

#------------------------------ sᴇcoɴᴅ vᴇʀɪғʏ --------------------------

2ND_VERIFY_SHORTNER = bool(environ.get('2ND_VERIFY_SHORTNER', False)) # sᴇᴛ True ᴏʀ False
2ND_VERIFY_SHORTLINK_URL = environ.get('2ND_VERIFY_SHORTLINK_URL', '') 

2ND_VERIFY_SHORTLINK_API = environ.get('2ND_VERIFY_SHORTLINK_API', '') 

#--------------------------------- oᴛʜᴇʀ --------------------------------

MAX_B_TN = environ.get("MAX_B_TN", "7")
MAX_BTN = is_enabled((environ.get('MAX_BTN', "True")), True)
PORT = environ.get("PORT", "8080")
IS_TUTORIAL = bool(environ.get('IS_TUTORIAL', True))
MSG_ALRT = environ.get('MSG_ALRT', '…👻')
P_TTI_SHOW_OFF = is_enabled((environ.get('P_TTI_SHOW_OFF', "False")), False)
IMDB = is_enabled((environ.get('IMDB', "False")), False)
AUTO_FFILTER = is_enabled((environ.get('AUTO_FFILTER', "True")), True)
AUTO_DELETE = is_enabled((environ.get('AUTO_DELETE', "True")), True)
NO_RESULTS_MSG = bool(environ.get("NO_RESULTS_MSG", False)) # "True" ɪꜰ ʏoᴜ want ɴo ʏoᴜ ʀᴇsᴜʟᴛs ᴍᴇꜱꜱᴀɢᴇs ɪɴ ʟoɢ cʜᴀɴɴᴇʟ ᴇʟsᴇ "False"

BUTTON_MODE = is_enabled((environ.get('BUTTON_MODE', "True")), True)
CUSTOM_FILE_CAPTION = environ.get("CUSTOM_FILE_CAPTION", f"{script.CAPTION}")
BATCH_FILE_CAPTION = environ.get("BATCH_FILE_CAPTION", CUSTOM_FILE_CAPTION)
WELCOME_TEXT = environ.get("WELCOME_TEXT", f"{script.WELCOME_TXT}")
IMDB_TEMPLATE = environ.get("IMDB_TEMPLATE", f"{script.IMDB_TEMPLATE_TXT}")
LONG_IMDB_DESCRIPTION = is_enabled(environ.get("LONG_IMDB_DESCRIPTION", "False"), False)
SPELL_CHECK_REPLY = is_enabled(environ.get("SPELL_CHECK_REPLY", "True"), True)
MAX_LIST_ELM = environ.get("MAX_LIST_ELM", None)
INDEX_REQ_CHANNEL = int(environ.get('INDEX_REQ_CHANNEL', LOG_CHANNEL))
MELCOW_NEW_USERS = is_enabled((environ.get('MELCOW_NEW_USERS', "True")), True)
PROTECT_CONTENT = is_enabled((environ.get('PROTECT_CONTENT', "True")), True)
PUBLIC_FILE_STORE = is_enabled((environ.get('PUBLIC_FILE_STORE', "True")), True)

LANGUAGES = ["malayalam", "", "tamil", "", "english", "", "hindi", "", "telugu", "", "kannada", "", "gujarati", "", "marathi", "", "punjabi", "", "bengali", ""]

SEASONS = ["season 1" , "season 2" , "season 3" , "season 4", "season 5" , "season 6" , "season 7" , "season 8" , "season 9" , "season 10"]

YEARS = ["1980" , "1981" , "1982" , "1983" , "1984" , "1985" , "1986" , "1987" , "1988" , "1989" , "1990" , "1991" , "1992" , "1993" , "1994" , "1995" , "1996" , "1997" , "1998" , "1999" , "2000" , "2001" , "2002" , "2003" , "2004" , "2005" , "2006" , "2007" , "2008" , "2009" , "2010" , "2011" , "2012" , "2013" , "2014" , "2015" , "2016" , "2017" , "2018" , "2019" , "2020" , "2021" , "2022" , "2023" , "2024" , "2025"]

QUALITIES = ["360P", "", "480P", "", "720P", "", "1080P", "", "1440P", "", "2160P", ""]

#----------------------- ᴏɴʟɪɴᴇ sᴛʀᴇᴀᴍ ᴀɴᴅ ᴅᴏᴡɴʟᴏᴀᴅ ----------------------

STREAM_MODE = bool(environ.get('STREAM_MODE', False)) # sᴇᴛ True ᴏʀ False
                                # sᴇᴛ sᴛʀᴇᴀᴍ ᴍoᴅᴇ "True" ᴛʜᴇɴ, ᴍᴜsᴛ ғɪʟʟ ᴜʀʟ !!                  
MULTI_CLIENT = False                        
SLEEP_THRESHOLD = int(environ.get('SLEEP_THRESHOLD', '60'))
PING_INTERVAL = int(environ.get("PING_INTERVAL", "1200"))  # 20 minutes
if 'DYNO' in environ:
    ON_HEROKU = True
else:
    ON_HEROKU = False
URL = environ.get("URL", "")   # ᴜʀʟ sᴛᴀʀᴛs wɪᴛʜ "https://" ᴀɴᴅ ᴇɴᴅs wɪᴛʜ "/"
                              # ʟɪᴋᴇ - https://super-bot-nixbotz-786.koyeb.app/

#----------------------------- ᴀᴜᴛo ᴀᴘᴘʀᴏᴠᴇ ------------------------------

APPROVED = environ.get("APPROVED_WELCOME", "on")

# ɢɪvᴇ wʜo cʜᴀᴛ ɪᴅ wʜᴇʀᴇ ʏoᴜ wᴀɴᴛ ʙᴏᴛ ᴀᴜᴛoᴍᴀᴛɪcᴀʟʟʏ ᴀᴜᴛo ᴀᴘᴘʀᴏᴠᴇᴅ ᴜsᴇʀs.
CHAT_ID = [int(app_chat_id) if id_pattern.search(app_chat_id) else app_chat_id for app_chat_id in environ.get('CHAT_ID', '').split()]
APPROVED_TEXT = environ.get("APPROVED_TEXT", f"<b>ʜᴇʟʟo {mention},\nʏᴏᴜʀ ʀᴇǫᴜᴇsᴛ ᴛᴏ ᴊᴏɪɴ {title} ɪs ᴀᴘᴘʀᴏᴠᴇᴅ ʙʏ <a href='https://telegram.me/Movies_Lisa_Robot'>ʟɪsᴀ</a> ᴡᴇʟᴄᴏᴍᴇ ᴛᴏ {title}\n\n⚡ ᴘᴏᴡᴇʀᴇᴅ ʙʏ : <a href='https://telegram.me/NIXBOTZ'>ɴɪsʜᴀɴᴛ</a></b>""")

#-----------------------------------••••••••••••••••-------------------------------

# ᴄʀᴇᴅɪᴛ - @NIXBOTZ
# ᴘʟᴇᴀsᴇ ᴅᴏɴ'ᴛ ʀᴇᴍᴏᴠᴇ ᴄʀᴇᴅɪᴛ..
# ғᴏʀ ᴀɴʏ ᴇʀʀᴏʀ/ᴅᴏᴜʙᴛ ᴘʟᴇᴀsᴇ ᴄᴏɴᴛᴀᴄᴛ ᴍᴇ oɴ ᴛᴇʟᴇɢʀᴀᴍ - @IM_NISHANTT

#-----------------------------------••••••••••••••••-------------------------------