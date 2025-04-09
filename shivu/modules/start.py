import random
from html import escape 

from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import CallbackContext, CallbackQueryHandler, CommandHandler

from shivu import application, SUPPORT_CHAT, UPDATE_CHAT, BOT_USERNAME, db, GROUP_ID
from shivu import pm_users as collection 

# Alag lists for gifs
PHOTO_URL_PM = [
    "https://media0.giphy.com/media/BfevCgt1YxDTW/giphy.gif",
    "https://media4.giphy.com/media/6sv3Z8wXzyEzC/giphy.gif",
    "https://media4.giphy.com/media/5D8fDjKyQfuZW/giphy.gif"
]

PHOTO_URL_GC = [
    "https://media2.giphy.com/media/HXN6ZE2FbnH44/giphy.gif",
    "https://media1.giphy.com/media/bJ0TSiVhirmlG/giphy.gif",
    "https://media0.giphy.com/media/8SEnoMhrEeBDa/giphy.gif"
]

async def start(update: Update, context: CallbackContext) -> None:
    user_id = update.effective_user.id
    first_name = update.effective_user.first_name
    username = update.effective_user.username

    user_data = await collection.find_one({"_id": user_id})

    if user_data is None:
        await collection.insert_one({"_id": user_id, "first_name": first_name, "username": username})
        await context.bot.send_message(chat_id=GROUP_ID, 
                                       text=f"New user Started The Bot..\nUser: <a href='tg://user?id={user_id}'>{escape(first_name)}</a>", 
                                       parse_mode='HTML')
    else:
        if user_data['first_name'] != first_name or user_data['username'] != username:
            await collection.update_one({"_id": user_id}, {"$set": {"first_name": first_name, "username": username}})

    keyboard = [
        [InlineKeyboardButton("ADD ME", url=f'http://t.me/{BOT_USERNAME}?startgroup=new')],
        [InlineKeyboardButton("SUPPORT", url=f'https://t.me/{SUPPORT_CHAT}'),
         InlineKeyboardButton("UPDATES", url=f'https://t.me/{UPDATE_CHAT}')],
        [InlineKeyboardButton("HELP", callback_data='help')],
        [InlineKeyboardButton("SOURCE", url=f'https://github.com/MyNameIsShekhar/WAIFU-HUSBANDO-CATCHER')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    if update.effective_chat.type == "private":
        caption = """
✨ **Summoning Jutsu Activated!** ✨  
I’m not just a bot...  
**I’m the gatekeeper to your legendary Harem.**

**Here’s what I do:**
— After every **100 messages** in your group  
— I drop a **random anime character** (yes, even rare ones!)  
— First to use **/guess** wins them  
— Build your collection, trade, gift, flex with **/harem**, **/top**, and more

**BUT WAIT...**

This isn’t just a game —  
This is your rise to becoming the **Harem King/Queen**.

**So what now?**
Just one click...  
Unleash the madness. Rule the waifu world.

**[ + ] Add Me To Your Group**  
Let the hunt begin!
"""
        photo_url = random.choice(PHOTO_URL_PM)
    else:
        caption = "🎴Alive!?... \nConnect to me in PM for more information"
        photo_url = random.choice(PHOTO_URL_GC)

    await context.bot.send_photo(chat_id=update.effective_chat.id, photo=photo_url, caption=caption, reply_markup=reply_markup, parse_mode='markdown')

# Handler registration
application.add_handler(CommandHandler('start', start, block=False))
