from pyrogram import Client, filters
from info import ADMINS, DATABASE_URI
from pyrogram.types import ReplyKeyboardMarkup
import asyncio
from database.topdb import NITopDB

movie_series_db = NITopDB(DATABASE_URI)
    

@Client.on_message(filters.command("setlist") & filters.private & filters.user(ADMINS))
async def set_movie_series_names_command(client, message):
  
    try:
        command, *names = message.text.split(maxsplit=1)
    except ValueError:
        await message.reply("Pʟᴇᴀsᴇ ᴘʀᴏᴠɪᴅᴇ ᴀ ʟɪsᴛ ᴏғ ᴍᴏᴠɪᴇ ᴀɴᴅ sᴇʀɪᴇs ɴᴀᴍᴇs ᴀғᴛᴇʀ ᴛʜᴇ ᴄᴏᴍᴍᴀɴᴅ.")
        return

    if not names:
        await message.reply("Pʟᴇᴀsᴇ ᴘʀᴏᴠɪᴅᴇ ᴀ ʟɪsᴛ ᴏғ ᴍᴏᴠɪᴇ ᴀɴᴅ sᴇʀɪᴇs ɴᴀᴍᴇs ᴀғᴛᴇʀ ᴛʜᴇ ᴄᴏᴍᴍᴀɴᴅ.")
        return

    names_string = " ".join(names)

    capitalized_names = ", ".join(" ".join(word.capitalize() for word in name.split()) for name in names_string.split(','))

    await movie_series_db.set_movie_series_names(capitalized_names, 1)

    await message.reply("Tʜᴇ ʟɪsᴛ ᴏғ ᴍᴏᴠɪᴇ ᴀɴᴅ sᴇʀɪᴇs ɴᴀᴍᴇs ғᴏʀ ᴛʜᴇ sᴜɢɢᴇsᴛɪᴏɴ ʜᴀs ʙᴇᴇɴ ᴜᴘᴅᴀᴛᴇᴅ sᴜᴄᴄᴇssғᴜʟʟʏ ✅")

@Client.on_message(filters.command("trendlist"))
async def get_movie_series_names_command(client, message):
    current_names = await movie_series_db.get_movie_series_names(1)

    if current_names:
        response = "<b><u>Cᴜʀʀᴇɴᴛ ʟɪsᴛ ᴏғ ᴛᴏᴘ ᴛʀᴇɴᴅɪɴɢ:</u></b>\n"
        for i, name in enumerate(current_names, start=1):
            response += f"{i}. {name}\n"
        await message.reply(response.strip())
    else:
        await message.reply("Tʜᴇ ʟɪsᴛ ᴏғ ᴛᴏᴘ ᴛʀᴇɴᴅɪɴɢ ғᴏʀ ʙᴜᴛᴛᴏɴs ᴀʀᴇ ᴇᴍᴘᴛʏ ❌")

@Client.on_message(filters.command("clearlist") & filters.private & filters.user(ADMINS))
async def clear_movie_series_names_command(client, message):
    await movie_series_db.clear_movie_series_names(1)
    await message.reply("Tʜᴇ ᴛᴏᴘ ᴛʀᴇɴᴅɪɴɢ ʟɪsᴛ ʜᴀs ʙᴇᴇɴ ᴄʟᴇᴀʀᴇᴅ sᴜᴄᴄᴇssғᴜʟʟʏ ✅")

@Client.on_message(filters.command("trend"))
async def trending_command(client, message):
  
    movie_series_names = await movie_series_db.get_movie_series_names(1)
    
    if not movie_series_names:
        await message.reply("Tʜᴇʀᴇ ᴀʀᴇ ɴᴏ ᴍᴏᴠɪᴇ ᴏʀ sᴇʀɪᴇs ɴᴀᴍᴇs ᴀᴠᴀɪʟᴀʙʟᴇ ғᴏʀ ᴛʜᴇ ᴛᴏᴘ sᴇᴀʀᴄʜᴇs.")
        return

    buttons = [movie_series_names[i:i + 2] for i in range(0, len(movie_series_names), 2)]

    spika = ReplyKeyboardMarkup(
        buttons,
        resize_keyboard=True
    )
    m=await message.reply_text("Pʟᴇᴀsᴇ wᴀɪᴛ, ғᴇᴛcʜɪɴɢ ᴛᴏᴘ ᴛʀᴇɴᴅɪɴɢ...")
    await m.delete()        
    await message.reply("<b>Hᴇʀᴇ ɪꜱ ᴛʜᴇ ᴛᴏᴘ ᴛʀᴇɴᴅɪɴɢ ʟɪꜱᴛ 👇</b>", reply_markup=spika)
