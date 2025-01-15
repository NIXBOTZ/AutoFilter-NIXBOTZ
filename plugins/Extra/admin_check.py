from pyrogram.types import Message
from pyrogram import filters, enums 


async def admin_check(message: Message) -> bool:
    if not message.from_user:
        return False

    if message.chat.type not in [enums.ChatType.GROUP, enums.ChatType.SUPERGROUP]:
        return False

    if message.from_user.id in [
        777000,  # Telegram Service Notifications
        1087968824  # GroupAnonymousBot
    ]:
        return True

    client = message._client
    chat_id = message.chat.id
    user_id = message.from_user.id

    check_status = await client.get_chat_member(
        chat_id=chat_id,
        user_id=user_id
    )
    admin_strings = [enums.ChatMemberStatus.OWNER, enums.ChatMemberStatus.ADMINISTRATOR]
    # https://git.colinshark.de/PyroBot/PyroBot/src/branch/master/pyrobot/modules/admin.py#L69
    if check_status.status not in admin_strings:
        return False
    else:
        return True

async def admin_filter_f(filt, client, message):
    return await admin_check(message)

admin_fliter = filters.create(func=admin_filter_f, name="AdminFilter")


# ᴛʜᴀɴᴋ ʏᴏᴜ ɴɪxʙᴏᴛz™ ғᴏʀ ʜᴇʟᴘɪɴɢ ᴜs ɪɴ ᴛʜɪs ᴊᴏᴜʀɴᴇʏ 
# ᴛʜᴀɴᴋ ʏᴏᴜ ғᴏʀ ɢɪᴠɪɴɢ ᴍᴇ ᴄʀᴇᴅɪᴛ 
# ᴄʀᴇᴅɪᴛ - @NIXBOTZ
# ᴘʟᴇᴀsᴇ ᴅᴏɴ'ᴛ ʀᴇᴍᴏᴠᴇ ᴄʀᴇᴅɪᴛ..
# ғᴏʀ ᴀɴʏ ᴇʀʀᴏʀ/ᴅᴏᴜʙᴛ ᴘʟᴇᴀsᴇ ᴄᴏɴᴛᴀᴄᴛ ᴍᴇ oɴ ᴛᴇʟᴇɢʀᴀᴍ - @IM_NISHANTT
#------------------------ 👻👻👻👻👻👻👻 -------------------------
