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
    welcome_message = """👋 Welcome to the SIM DAC community! We are thrilled to have you join us! 🤗

Our community is a place where like-minded individuals 👥 gather together to share knowledge, ideas & experiences related to the field of data! 💻👩‍💻 Whether you are an expert or beginner, you will find a supportive group here. Introduce yourself in #Community Center & share your interests!

Here are a few tips to make the most of our community:
🏫 Check out the #Curriculum channel for the curriculum taught and led by the DAC Excos
📚 Check out our #Github links for helpful guides, tutorials, and recommended reading materials.
🗓️ Keep an eye on the #Events channel for upcoming meetups, workshops, recruitment cycle, and other exciting activities! 
📢 Use the appropriate channels to discuss specific topics, and don't hesitate to ask questions or share your insights.
🤝 Be respectful and supportive of others, regardless of their backgrounds or skill levels.

Once again, welcome aboard! We're excited to have you here and look forward to you joining us! 🎉

If you have any questions! We're always happy to help! Feel free to reach out to one of the EXCOS. Feeling shy to speak up in the channel 🙈 feel free to talk to our @Q&A_bot !"""
    
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
