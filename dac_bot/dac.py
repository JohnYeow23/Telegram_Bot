import os
import logging #this helps with tracking the chat logs from telegram
import telebot

from typing import Optional, Tuple
from dotenv import load_dotenv
from telegram import Chat, Chatmember, ChatMemberUpdated, Update
from telegram.constants import ParseMode
from telegram .ext import(
    Application
    , ChatMemberHandler
    , CommandHandler
    , ContextTypes
    , MessagesHandler
    , filters
) 

load_dotenv()

# Enabling logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

# set higher logging level for httpx to avoid all GET and POST requests being logged
logging.getLogger("httpx").setLevel(logging.WARNING)

logger = logging.getLogger(__name__)

BOT_TOKEN = os.environ.get('BOT_TOKEN')
bot = telebot.TeleBot(BOT_TOKEN)

def extract_status_change(chat_member_update: ChatMemberUpdated) -> Optional[Tuple[bool, bool]]:
    """Takes a ChatMemberUpdated instance and extracts whether the 'old_chat_member' was a member
    of the chat and whether the 'new_chat_member' is a member of the chat. Returns None, if
    the status didn't change.
    """
    status_change = chat_member_update.difference().get("status")
    old_is_member, new_is_member = chat_member_update.difference().get("is_member",(None, None))

@bot.message_handler(commands=['start', 'hello'])
def greet_new_joiners(message):
    welcome_message = """👋 A warm welcome to the SIM DAC community! We're delighted you're here! 🤗
    \nThis community is a haven for individuals 👥 with a shared passion for everything data-related! 💻👩‍💻 Irrespective of your experience level, our group provides a supportive platform where you can interact, learn, and grow. Take a moment to introduce yourself in the #Community Center and share what excites you about data!
    \nTo help you settle in, here are a few pointers:
    \n🏫 Explore the *Curriculum* channel to get acquainted with our DAC Excos-led program.
    📚 Visit our *Github* links for insightful guides, tutorials, and resources.
    🗓️ Keep the *Events* channel on your radar for not-to-be-missed meetups, workshops, recruitment drives, and more! 
    📢 Make use of designated channels for topic-related discussions and never hold back if you need assistance!
    🤝 Promote an environment of respect and support, appreciating the diverse backgrounds and varying skill levels within our community. 
    \nWe're thrilled to have you with us, and we can't wait for you to be part of our exciting journey! 🎉 
    \nRemember, we're here to help! Any questions or concerns, feel free to approach any of the EXCOS or speak directly to our @Q&A_bot if you prefer a more private conversation. Once again, welcome aboard!
    """

    bot.reply_to(
        message,
        welcome_message,
        parse_mode="None"
    )

#Saving these codes for later
    # keyboard = types.InlineKeyboardMarkup()
    # start_button = types.InlineKeyboardButton(text="/start", callback_data="/start:Get started with the bot")
    # info_button = types.InlineKeyboardButton(text="/info", callback_data="/info:Get information about the bot")
    # keyboard.add(start_button, info_button)
    
    # @bot.callback_query_handler(func=lambda _: True)
    # def handle_callback(call):
    #    command, description = call.data.split(":")
    #    if command == "/start":
    #        bot.send_message(call.message.chat.id, f"You clicked the '/start' button.\n\n{description}")
    #        # bot.reply_to("This is a brief introduction to DAC and it's purpose!")
    #    elif command == "/info":
    #        bot.send_message(call.message.chat.id, f"You clicked the '/info' button.\n\n{description}")
    #        # bot.reply_to("Here are the relevant materials for DAC that you can go and take a read!")


bot.infinity_polling()