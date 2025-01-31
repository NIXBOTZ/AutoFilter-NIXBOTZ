# ᴄʀᴇᴅɪᴛ - @NIXBOTZ
# ᴘʟᴇᴀsᴇ ᴅᴏɴ'ᴛ ʀᴇᴍᴏᴠᴇ ᴄʀᴇᴅɪᴛ..
# ғᴏʀ ᴀɴʏ ᴇʀʀᴏʀ/ᴅᴏᴜʙᴛ ᴘʟᴇᴀsᴇ ᴄᴏɴᴛᴀᴄᴛ ᴍᴇ oɴ ᴛᴇʟᴇɢʀᴀᴍ - @IM_NISHANTT

from pyrogram import Client, filters
from pyrogram.types import Message

@Client.on_message(filters.command("groupinfo", prefixes="/"))
async def get_group_status(_, message: Message):
    if len(message.command) != 2:
        await message.reply("Please provide a group username. Example: `/groupinfo YourGroupUsername`")
        return
    
    group_username = message.command[1]
    
    try:
        group = await Client.get_chat(group_username)
    except Exception as e:
        await message.reply(f"Error: {e}")
        return
    
    total_members = await Client.get_chat_members_count(group.id)
    group_description = group.description
    premium_acc = banned = deleted_acc = bot = 0  # You should replace these variables with actual counts.

    response_text = (
        f"------------------------ ɢʀᴏᴜᴩ ᴅᴀᴛᴀ ----------------------\n\n"
        f"➲ ɢʀᴏᴜᴩ ɴᴀᴍᴇ : {group.title} ✅\n"
        f"➲ ɢʀᴏᴜᴩ ɪᴅ : {group.id}\n"
        f"➲ ᴛoᴛᴀʟ ᴍᴇᴍʙᴇʀs : {total_members}\n"
        f"➲ ᴅᴇscʀɪᴩᴛɪoɴ : {group_description or 'N/A'}\n"
        f"➲ ᴜsᴇʀɴᴀᴍᴇ : @{group_username}\n"
       
        f"⚡ ᴘᴏᴡᴇʀᴇᴅ ʙʏ : <a href='https://t.me/NIXBOTZ'>ɴɪsʜᴀɴᴛ</a>"
    )
    
    await message.reply(response_text)






# Command handler to get group status
@Client.on_message(filters.command("status") & filters.group)
def group_status(client, message):
    chat = message.chat  # Chat where the command was sent
    status_text = f"ɢʀᴏᴜᴩ ɪᴅ: {chat.id}\n" \
                  f"ᴛɪᴛʟᴇ: {chat.title}\n" \
                  f"ᴛʏᴘᴇ: {chat.type}\n"
                  
    if chat.username:  # Not all groups have a username
        status_text += f"Username: @{chat.username}"
    else:
        status_text += "ᴜsᴇʀɴᴀᴍᴇ: None"

    message.reply_text(status_text)



# ᴄʀᴇᴅɪᴛ - @NIXBOTZ
# ᴘʟᴇᴀsᴇ ᴅᴏɴ'ᴛ ʀᴇᴍᴏᴠᴇ ᴄʀᴇᴅɪᴛ..
# ғᴏʀ ᴀɴʏ ᴇʀʀᴏʀ/ᴅᴏᴜʙᴛ ᴘʟᴇᴀsᴇ ᴄᴏɴᴛᴀᴄᴛ ᴍᴇ oɴ ᴛᴇʟᴇɢʀᴀᴍ - @IM_NISHANTT
