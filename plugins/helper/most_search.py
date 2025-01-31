import re
from pyrogram import Client, filters
from pyrogram.types import ReplyKeyboardMarkup
from database.config_db import mdb

@Client.on_message(filters.command('most'))
async def most(client, message):

    def is_alphanumeric(string):
        return bool(re.match('^[a-zA-Z0-9 ]*$', string))
    
    try:
        limit = int(message.command[1])
    except (IndexError, ValueError):
        limit = 20

    top_messages = await mdb.get_top_messages(limit)
    seen_messages = set()
    truncated_messages = []

    for msg in top_messages:
        
        if msg.lower() not in seen_messages and is_alphanumeric(msg):
            seen_messages.add(msg.lower())
            
            if len(msg) > 35:
                truncated_messages.append(msg[:35 - 3])
            else:
                truncated_messages.append(msg)

    keyboard = []
    for i in range(0, len(truncated_messages), 2):
        row = truncated_messages[i:i+2]
        keyboard.append(row)
    
    reply_markup = ReplyKeyboardMarkup(keyboard, one_time_keyboard=True, resize_keyboard=True, placeholder="Most searches of the day")
    m=await message.reply_text("ɪ'ᴍ ғᴇᴛcʜɪɴɢ ᴍᴏꜱᴛ ꜱᴇᴀʀᴄʜᴇꜱ oғ ᴛoᴅᴀ𝚈 👩🏻‍💻")
    await m.edit_text("Pʟᴇᴀsᴇ wᴀɪᴛ...")
    await m.delete()
    await message.reply_text(f"<b>Hᴇʀᴇ ɪꜱ ᴛʜᴇ ᴍᴏꜱᴛ ꜱᴇᴀʀᴄʜᴇꜱ ʟɪꜱᴛ 👇</b>", reply_markup=reply_markup)

    
@Client.on_message(filters.command('mostlist'))
async def trendlist(client, message):
    def is_alphanumeric(string):
        return bool(re.match('^[a-zA-Z0-9 ]*$', string))


    limit = 31

 
    if len(message.command) > 1:
        try:
            limit = int(message.command[1])
        except ValueError:
            await message.reply_text("Invalid number format.\nPlease provide a valid number after the /mostlist command.")
            return  

    try:
        top_messages = await mdb.get_top_messages(limit)
    except Exception as e:
        await message.reply_text(f"Error retrieving messages: {str(e)}")
        return  

    if not top_messages:
        await message.reply_text("ɴo ᴍᴏꜱᴛ ꜱᴇᴀʀᴄʜᴇꜱ ᴍᴇssᴀɢᴇꜱ ғoᴜɴᴅ 🚫")
        return  
    seen_messages = set()
    truncated_messages = []

    for msg in top_messages:
        if msg.lower() not in seen_messages and is_alphanumeric(msg):
            seen_messages.add(msg.lower())
            

            truncated_messages.append(msg[:32] + '...' if len(msg) > 35 else msg)

    if not truncated_messages:
        await message.reply_text("No valid most messages found.")
        return  
  
    formatted_list = "\n".join([f"{i+1}. <b>{msg}</b>" for i, msg in enumerate(truncated_messages)])
   
    additional_message = "𝑨𝒍𝒍 𝒕𝒉𝒆 𝒓𝒆𝒔𝒖𝒍𝒕𝒔 𝒂𝒃𝒐𝒗𝒆 𝒄𝒐𝒎𝒆 𝒇𝒓𝒐𝒎 𝒘𝒉𝒂𝒕 𝒖𝒔𝒆𝒓𝒔 𝒉𝒂𝒗𝒆 𝒔𝒆𝒂𝒓𝒄𝒉𝒆𝒅 𝒇𝒐𝒓. 𝑻𝒉𝒆𝒚'𝒓𝒆 𝒔𝒉𝒐𝒘𝒏 𝒕𝒐 𝒚𝒐𝒖 𝒆𝒙𝒂𝒄𝒕𝒍𝒚 𝒂𝒔 𝒕𝒉𝒆𝒚 𝒘𝒆𝒓𝒆 𝒔𝒆𝒂𝒓𝒄𝒉𝒆𝒅, 𝒘𝒊𝒕𝒉𝒐𝒖𝒕 𝒂𝒏𝒚 𝒄𝒉𝒂𝒏𝒈𝒆𝒔 𝒃𝒚 𝒕𝒉𝒆 𝒐𝒘𝒏𝒆𝒓."
    formatted_list += f"\n\n{additional_message}"

    reply_text = f"<b><u>Top {len(truncated_messages)} Most Searches List:</u></b>\n\n{formatted_list}"
    
    await message.reply_text(reply_text)
    
    
# ᴄʀᴇᴅɪᴛ - @NIXBOTZ
# ᴘʟᴇᴀsᴇ ᴅᴏɴ'ᴛ ʀᴇᴍᴏᴠᴇ ᴄʀᴇᴅɪᴛ..
# ғᴏʀ ᴀɴʏ ᴇʀʀᴏʀ/ᴅᴏᴜʙᴛ ᴘʟᴇᴀsᴇ ᴄᴏɴᴛᴀᴄᴛ ᴍᴇ oɴ ᴛᴇʟᴇɢʀᴀᴍ - @IM_NISHANTT