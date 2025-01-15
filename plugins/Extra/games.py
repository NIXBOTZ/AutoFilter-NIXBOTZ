from pyrogram import Client, filters, enums
from utils import f_onw_fliter
import asyncio
import requests
from requests import get
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from utils import temp


# EMOJI CONSTANTS
DART_E_MOJI = "🎯"
# EMOJI CONSTANTS
CMD = ["/", "."]

@Client.on_message(
    filters.command(["throw", "dart"], CMD) &
    f_onw_fliter
)
async def throw_dart(client, message):
    """ /throw an @AnimatedDart """
    rep_mesg_id = message.id
    if message.reply_to_message:
        rep_mesg_id = message.reply_to_message.id
    await client.send_dice(
        chat_id=message.chat.id,
        emoji=DART_E_MOJI,
        disable_notification=True,
        reply_to_message_id=rep_mesg_id
    )

# EMOJI CONSTANTS
DICE_E_MOJI = "🎲"
# EMOJI CONSTANTS

@Client.on_message(
    filters.command(["roll", "dice"], CMD) &
    f_onw_fliter
)
async def roll_dice(client, message):
    """ @RollaDie """
    rep_mesg_id = message.id
    if message.reply_to_message:
        rep_mesg_id = message.reply_to_message.id
    await client.send_dice(
        chat_id=message.chat.id,
        emoji=DICE_E_MOJI,
        disable_notification=True,
        reply_to_message_id=rep_mesg_id
    )
    
 # EMOJI CONSTANTS
GOAL_E_MOJI = "⚽"
# EMOJI CONSTANTS

@Client.on_message(
    filters.command(["goal", "shoot"], CMD) &
    f_onw_fliter
)
async def roll_dice(client, message):
    """ @Goal """
    rep_mesg_id = message.id
    if message.reply_to_message:
        rep_mesg_id = message.reply_to_message.id
    await client.send_dice(
        chat_id=message.chat.id,
        emoji=GOAL_E_MOJI,
        disable_notification=True,
        reply_to_message_id=rep_mesg_id
    )
    
# EMOJI CONSTANTS
TRY_YOUR_LUCK = "🎰"
# EMOJI CONSTANTS

@Client.on_message(
    filters.command(["luck", "cownd"] CMD)
)
async def luck_cownd(client, message):
    """ /luck an @animatedluck """
    rep_mesg_id = message.id
    if message.reply_to_message:
        rep_mesg_id = message.reply_to_message.id
    await client.send_dice(
        chat_id=message.chat.id,
        emoji=TRY_YOUR_LUCK,
        disable_notification=True,
        reply_to_message_id=rep_mesg_id
    )
    
@Client.on_message(filters.command("write"))
async def handwrite(_, message: Message):
    if not message.reply_to_message:
        text = message.text.split(None, 1)[1]
        m = await message.reply_text("<b>ᴘʟᴇᴀsᴇ ᴡᴀɪᴛ...</b>")
        API = f"https://api.sdbots.tk/write?text={text}"
        req = requests.get(API).url
        await message.reply_photo(
            photo=req,
            caption="""<b>✍  ʙʏ  -  <a href=https://telegram.me/IM_NISHANTT>𝙽 𝙸</a></b>""",
            reply_markup=InlineKeyboardMarkup(
                [[InlineKeyboardButton("📑    ᴛᴇʟᴇɢʀᴀᴘʜ  ʟɪɴᴋ    📑", url=f"{req}")]]
            ),
        )
        await m.delete()
        
        
# ᴛʜᴀɴᴋ ʏᴏᴜ ɴɪxʙᴏᴛz™ ғᴏʀ ʜᴇʟᴘɪɴɢ ᴜs ɪɴ ᴛʜɪs ᴊᴏᴜʀɴᴇʏ 
# ᴛʜᴀɴᴋ ʏᴏᴜ ғᴏʀ ɢɪᴠɪɴɢ ᴍᴇ ᴄʀᴇᴅɪᴛ 
# ᴄʀᴇᴅɪᴛ - @NIXBOTZ
# ᴘʟᴇᴀsᴇ ᴅᴏɴ'ᴛ ʀᴇᴍᴏᴠᴇ ᴄʀᴇᴅɪᴛ..
# ғᴏʀ ᴀɴʏ ᴇʀʀᴏʀ/ᴅᴏᴜʙᴛ ᴘʟᴇᴀsᴇ ᴄᴏɴᴛᴀᴄᴛ ᴍᴇ oɴ ᴛᴇʟᴇɢʀᴀᴍ - @IM_NISHANTT
#------------------------ 👻👻👻👻👻👻👻 -------------------------