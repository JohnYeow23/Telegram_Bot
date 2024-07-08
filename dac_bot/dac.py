import os
import telebot
from telebot import types
from dotenv import load_dotenv


load_dotenv()


BOT_TOKEN = os.environ.get('BOT_TOKEN')
bot = telebot.TeleBot(BOT_TOKEN)


# @bot.message_handler(commands=['start', 'hello'])
# def send_welcome(message):
#     bot.reply_to(message, "Hello fellow enthusiastic data scientist! How can I help you today?")


# @bot.chat_member_handler()
# def greet_new_joiners(message: types.ChatMemberUpdated):
@bot.message_handler(commands=['start', 'hello'])
def greet_new_joiners(message):
   welcome_message = """Welcome to the DAC Channel!!
   \nWe are glad to have you here! For the relevant information on DAC, you can control me by sending these commands:
   \n- **Curriculum**
   \n- **Github**
   \n- **Recruitment**
   \n- **Social Media**"""
  
   keyboard = types.InlineKeyboardMarkup()
   start_button = types.InlineKeyboardButton(text="/start", callback_data="/start:Get started with the bot")
   info_button = types.InlineKeyboardButton(text="/info", callback_data="/info:Get information about the bot")
   keyboard.add(start_button, info_button)


   bot.reply_to(
       message,
       welcome_message,
       reply_markup=keyboard,
       parse_mode="Markdown"
   )
      
@bot.callback_query_handler(func=lambda _: True)
def handle_callback(call):
   command, description = call.data.split(":")
   if command == "/start":
       bot.send_message(call.message.chat.id, f"You clicked the '/start' button.\n\n{description}")
       # bot.reply_to("This is a brief introduction to DAC and it's purpose!")
   elif command == "/info":
       bot.send_message(call.message.chat.id, f"You clicked the '/info' button.\n\n{description}")
       # bot.reply_to("Here are the relevant materials for DAC that you can go and take a read!")


bot.infinity_polling()
